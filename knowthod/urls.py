from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', redirect_blog),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('compiler/', include('compiler.urls')),
    path('contests/', include('contests.urls')),
    path('tasks/', include('tasks.urls'))
]
