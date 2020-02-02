"""
Очень важно, что если надо брать всех юзеро, то юзать вот это:
users = User.objects.all().select_related('profile')
"""

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.template import RequestContext

from .forms import *

class UserRegisterFormView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect('/')
        return render(request, self.template_name, context={'form': form})

class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль обновлен.')
            return redirect('/accounts/profile-update/')
        else:
            messages.error(request, 'Что-то пошло не так.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile_update.html', {'user_form':user_form, 'profile_form':profile_form})

@login_required
def profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'accounts/profile.html', {'u':user})

@login_required
def profile_friends_view(request, username):
    return render(request, 'accounts/profile_friends_view.html', {})

@login_required
def profile_find_friends(request, username):
    users = User.objects.all().select_related('profile')
    return render(request, 'accounts/profile_find_friends.html', {'users': users})
