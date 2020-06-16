from django.contrib import admin
from django.db import models



class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 200)
    nickname = models.CharField(max_length = 50,default='匿名')
    email = models.EmailField()

    def __str__(self):
        return self.username

class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间
    flag = models.AutoField(primary_key=True)   # 评论跟随

class BlogComments(models.Model):
    username = models.CharField(max_length = 50)
    c_content = models.CharField(max_length = 80)
    flag = models.IntegerField(max_length=100)

class ToDos(models.Model):
    completed = models.IntegerField(max_length=10)
    title = models.TextField()
    user = models.TextField()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
