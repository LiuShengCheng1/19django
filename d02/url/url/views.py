from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def login(request):
    next = request.GET.get('next')
    text = "登录页面，登录后跳转的页面" % next
    return HttpResponse(text)


def book_detail(request, book_id, category):
    text = "您要查询的"
