from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import auth
from .models import *

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username').lower()
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("Пользователь с таким именем уже зарегистрирован.")
        email = self.cleaned_data.get('email').lower()
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Пользователь с такой почтой уже зарегистрирован.")
        return super(UserRegisterForm, self).clean(*args, **kwargs)

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Не правильный логин или пароль.")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')
