#coding=utf-8

from django.db import models
from django.contrib import admin

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')



admin.site.register(BlogsPost,BlogPostAdmin)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

class BlogBody(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_type = models.CharField(max_length=50)
    blog_timestamp = models.DateTimeField()
    blog_imgurl = models.CharField(max_length=50, null=True)
    blog_author = models.CharField(max_length=20)

