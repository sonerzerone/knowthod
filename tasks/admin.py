from django.contrib import admin

from .models import *

class TestAdmin(admin.ModelAdmin):
    list_display = ['input', 'output']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'body']

class SendAdmin(admin.ModelAdmin):
    list_display = ['sender', 'task', 'status']
    fields = ['task', 'sender', 'title', 'code', 'slug', 'status']

admin.site.register(Test, TestAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Send, SendAdmin)
