"""
obj = get_object_or_404(self.model, slug__iexact=slug)
t = Test.objects.filter(task=obj)
for tt in t:
    print(tt.input, tt.output)
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *

from compiler.utils import *

tasks_number_on_one_page = 3 # Кол-во постов на одной странице

def tasks_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        tasks = Task.objects.filter(Q(title__icontains=search_query.title()) | Q(title__icontains=search_query.lower()) | Q(body__icontains=search_query.title()) | Q(body__icontains=search_query.lower()))
    else:
        tasks = Task.objects.all()

    paginator = Paginator(tasks, tasks_number_on_one_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url
    }
    return render(request, 'tasks/tasks_view.html', context=context)

class TaskDetail(View):
    model = Task
    template = 'tasks/task_detail.html'

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower():obj, 'detail':True})

class TaskCreate(LoginRequiredMixin, View):
    model_form = TaskForm
    template = 'tasks/task_create_form.html'
    raise_exception = True

    def get(self, request):
        form = self.model_form()
        form2 = TaskJsonDataForm()
        return render(request, self.template, context={'form':form, 'form2':form2})

    def post(self, request):
        form = self.model_form(request.POST)
        form2 = TaskJsonDataForm(request.POST)
        if form.is_valid() and form2.is_valid():
            obj = form.save()
            obj2 = form2.cleaned_data.get('jsondata')

            import json
            data = json.loads(obj2)
            for test in data['tests']:
                testinput = test['input']
                testoutput = test['output']
                obj3 = Test.objects.create(task=obj, input=testinput, output=testoutput)
                obj3.save()


            return redirect(obj)
        return render(request, self.template, context={'form':form, 'form2':form2})

class TaskUpdate(LoginRequiredMixin, View):
    model = Task
    model_form = TaskForm
    template = 'tasks/task_update_form.html'
    raise_exception = True

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':form, self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.model_form(request.POST, instance=obj)

        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form':form, self.model.__name__.lower():obj})

class TaskDelete(LoginRequiredMixin, View):
    model = Task
    template = 'tasks/task_delete_form.html'
    redirect_url = 'tasks_view_url'
    raise_exception = True

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        return render(request, self.template, context={self.model.__name__.lower():obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj2 = Test.objects.filter(task=obj)
        obj2.delete()
        obj.delete()
        return redirect(reverse(self.redirect_url))

class TaskSend(View):
    model_form = SendForm
    template = 'tasks/task_send_form.html'
    raise_exception = True

    def get(self, request, slug):
        form = self.model_form()
        task = Task.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'form':form, 'task':task})

    def post(self, request, slug):
        form = self.model_form(request.POST)

        if form.is_valid():
            obj = form.save()
            user = User.objects.get(username=request.user.username)
            obj.sender = user
            obj.slug = gen_slug(user.username)
            obj.status = 'Ожидние'
            task = Task.objects.get(slug__iexact=slug)
            obj.task = task
            obj.title = user.username + ' - ' + obj.task.title
            obj = form.save()

            gerr = None
            tests = Test.objects.filter(task=task)
            for test in tests:
                run = RunCppCode(obj.code, test.input)
                rescomp, resrun = run.run_cpp_code()
                resrun = resrun.rstrip()
                resrun = resrun.lstrip()
                if rescomp != '':
                    gerr = rescomp
                    break
                elif resrun != test.output:
                    gerr = 'Ошибка на тесте: \n' + 'Входные данные: "' + test.input + '"\nВыходные данные: "' + test.output + '"\n' + 'Ваши выходные данные: "' + resrun + '"'

            if gerr == None:
                obj.status = 'Зачтено'
            else:
                obj.status = 'Ошибка'
                obj.error = gerr

            obj = form.save()

            
            return redirect(reverse('task_detail_url', kwargs={'slug':task.slug}))

        return render(request, self.template, context={'form':form, 'task':task})

class SendDetail(View):
    model = Send
    template = 'tasks/send_detail_form.html'

    def get(self, request, slug, slug2):
        obj = Send.objects.get(slug__iexact=slug2)
        #obj.task
        tests = Test.objects.filter(task=obj.task)
        return render(request, self.template, context={self.model.__name__.lower():obj, 'tests':tests})



sends_number_on_one_page = 3 # Кол-во сендов на одной странице

def sends_view(request, slug):
    #search_query = request.GET.get('search', '')
    #if search_query:
    #    sends = Send.objects.filter(Q(title__icontains=search_query.title()) | Q(title__icontains=search_query.lower()) | Q(body__icontains=search_query.title()) | Q(body__icontains=search_query.lower()))
    #else:
    #    sends = Send.objects.all()
    task = Task.objects.get(slug__iexact=slug)
    sends = Send.objects.filter(task=task)

    paginator = Paginator(sends, sends_number_on_one_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
        'task': task
    }
    return render(request, 'tasks/sends_view.html', context=context)


"""
# Пример вьюхи для формы без модели
def test(request):
    if request.method == 'POST':
        form = TestT(request.POST)
        if form.is_valid():
            obj = form.cleaned_data.get('test')
            print(obj)
    else:
        form = TestT()
    return render(request, 'tasks/test.html', {'form':form})
"""
