from django.urls import path

from .views import *

urlpatterns = [
    path('', compiler_view, name='compiler_view_url'),
    path('python/', CompilerPython.as_view(), name='compiler_python_url'),
    path('cpp/', CompilerCpp.as_view(), name='compiler_cpp_url')
]
