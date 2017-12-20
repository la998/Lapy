from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {'hello': 'Hello World xiaodidi!'}
    return render(request, 'hello.html', context)


def index(request):
    return HttpResponse("Index")
