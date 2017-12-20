"""Lapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import *
from . import view, blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view.index, name='index'),
    url(r'^hello$', view.hello),
    url(r'^save$', blog.save_blog),
    url(r'^get$', blog.get_blog),
    url(r'^update$', blog.update_blog),
    url(r'^delete$', blog.delete_blog)
]
