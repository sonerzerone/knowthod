from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *

def compiler_view(request):
    return render(request, 'compiler/compiler_view.html', {})

class CompilerPython(View):
    form_class = CompilerForm
    template_name = 'compiler/compiler_python.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            code = request.POST['code']
            input = request.POST['input']
            run = RunPyCode(code, input)
            rescompil, resrun = run.run_py_code()
            resrun=resrun
            rescomp=rescompil

            if not resrun:
                resrun = 'No result!'
        else:
            code = default_py_code
            resrun = 'No result!'
            rescompil = "No compilation for Python"

        return render (request,self.template_name, {'code':code, 'input':input,'resrun':resrun,'rescomp':rescomp})

class CompilerCpp(View):
    form_class = CompilerForm
    template_name = 'compiler/compiler_cpp.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            code = request.POST['code']
            input = request.POST['input']
            run = RunCppCode(code, input)
            rescompil, resrun = run.run_cpp_code()
            resrun=resrun
            rescomp=rescompil

            if not resrun:
                resrun = 'No result!'
        else:
            code = default_py_code
            resrun = 'No result!'
            rescompil = "No compilation for Python"

        return render (request,self.template_name, {'code':code, 'input':input,'resrun':resrun,'rescomp':rescomp})
