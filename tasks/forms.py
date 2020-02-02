from django import forms
from .models import *
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'slug', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug'].lower()

        if slug == 'create':
            raise ValidationError('Slug не может быть "create"')

        return slug

class SendForm(forms.ModelForm):
    class Meta:
        model = Send
        fields = ['code',]

        widgets = {
            'code': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SendDetailForm(forms.ModelForm):
    class Meta:
        model = Send
        fields = ['task', 'code', 'status', 'error']

    widgets = {
        'task': forms.TextInput(attrs={'class': 'form-control'}),
        'code': forms.Textarea(attrs={'class': 'form-control'}),
        'status': forms.TextInput(attrs={'class': 'form-control'}),
        'error': forms.Textarea(attrs={'class': 'form-control'}),
    }

# Пример формы без модели
#class TestT(forms.Form):
#    test = forms.CharField(label='test', max_length=100)

class TaskJsonDataForm(forms.Form):
    jsondata = forms.CharField(widget=forms.Textarea)

class TestForm(forms.Form):
    class Meta:
        model = Test
        fields = ['task', 'input', 'output']

    widgets = {
        'task': forms.TextInput(attrs={'class': 'form-control'}),
        'input': forms.TextInput(attrs={'class': 'form-control'}),
        'output': forms.TextInput(attrs={'class': 'form-control'}),
    }
