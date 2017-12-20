# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from WebModel.models import Blog


def save_blog(request):
    obj = Blog(title='Has saved!')
    obj.save()
    return HttpResponse('<p>数据添加成功</p>')
