"""PollApplication URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

# Point the root URLconf at the polls.urls module.
urlpatterns = [
	# include() allows referencing other URLconfs.
	# Whenever Django encounters include(), it removes whatever part of the URL
	# matched up to that point and sends the remaining string to the included
	# URLconf for further processing.
	# The idea behind it is to make it easy to plug-and-play URLs.
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]