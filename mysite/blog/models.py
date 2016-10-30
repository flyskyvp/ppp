
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