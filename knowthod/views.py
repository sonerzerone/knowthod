from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)




"""
from django.contrib.auth.decorators import login_required
@login_required
Это надо для того, чтобы ограниить вход не авторизированым юзерам.
Если чюзер не авторизирован, то его перебросит на страниуц авториации.
Если авторизирован, то то где указать @login_required, будет показано.
"""
