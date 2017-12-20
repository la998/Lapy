# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from WebModel.models import Blog


def save_blog(request):
    obj = Blog(title='yes saved!')
    obj.save()
    return HttpResponse('<p>数据添加成功</p>')


def get_blog(request):
    response = ""
    response1 = ""

    blog = Blog.objects.all()

    for b in blog:
        response1 += b.title + "<br>"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
