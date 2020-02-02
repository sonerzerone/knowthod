from django import forms
from django.core.exceptions import ValidationError
from .models import *

class CompilerForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ('code', 'input', 'resrun', 'rescomp')
