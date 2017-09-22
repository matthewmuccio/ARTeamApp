"""SimpleBlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# Importing models
from SimpleBlogApp.models import Tag, MyBlog

# Generic views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Makes model visible in admin system.
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ListView.as_view(model = MyBlog, template_name = 'blog_list.html'), name='blog_list'),
    url(r'^details/(?P<pk>[0-9]+)/', DetailView.as_view(model = MyBlog, template_name = 'blog_details.html'), name='blog_details'),
]