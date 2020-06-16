"""DemlutionBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/',include('blog.urls')),
    path('',views.index),
    path('login',views.login,name='login'),
    path('regist',views.regist,name='regist'),
    path('blog/<blogFlag>',views.display,name='blog'),
    path('comment',views.set_comment,name='comment'),
    path('bloglist',views.blog_list,name='bloglist'),
    path('todos',views.todo_post,name='todos'),
    path('insert',views.insert,name='insert'),
    path('del',views.del_todo,name='del'),
    path('change',views.change_status,name='change'),
    path('active',views.active,name='active'),
    path('completed',views.completed,name='completed'),
]
