from django.http import HttpResponse
from django.shortcuts import redirect


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        return redirect('/login/')


def login(request):
    return HttpResponse("前台登录页")
