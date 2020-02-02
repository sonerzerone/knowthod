from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterFormView.as_view(), name='register_url'),
    path('login/', UserLoginFormView.as_view(), name='login_url'),
    path('logout/', logout_view, name='logout_url'),
    path('profile-update/', profile_update, name='profile_update_url'),
    path('profile/<str:username>/', profile_view, name='profile_view_url'),
    path('profile/<str:username>/friends', profile_friends_view, name='profile_friends_view_url'),
    path('profile/<str:username>/find_friends', profile_find_friends, name='profile_friends_find_url')
]
