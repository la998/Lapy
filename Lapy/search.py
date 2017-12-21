#!/usr/bin python
# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf


def search_form(request):
    return render_to_response("search.html")


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = "search key:" + request.GET['q']
    else:
        message = "search null"
    return HttpResponse(message)


def search_post(request):
    request.encoding = 'utf-8'
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)