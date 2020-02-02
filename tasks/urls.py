from django.urls import path

from .views import *

urlpatterns = [
    path('', tasks_view, name='tasks_view_url'),
    path('task/create/', TaskCreate.as_view(), name='task_create_url'),
    path('task/<str:slug>/', TaskDetail.as_view(), name='task_detail_url'),
    path('task/<str:slug>/update/', TaskUpdate.as_view(), name='task_update_url'),
    path('task/<str:slug>/delete/', TaskDelete.as_view(), name='task_delete_url'),
    path('task/<str:slug>/send/', TaskSend.as_view(), name='task_send_url'),
    path('task/<str:slug>/sends/', sends_view, name='sends_view_url'),
    path('task/<str:slug>/sends/<str:slug2>/', SendDetail.as_view(), name='send_detail_url'),
    #path('test/', test, name='test_url')
]
