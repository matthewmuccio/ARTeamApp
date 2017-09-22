from django.contrib import admin
from django import forms

from SimpleBlogApp.models import MyBlog, Tag

# Registers MyBlog and Tag models here.
admin.site.register(MyBlog)
admin.site.register(Tag)