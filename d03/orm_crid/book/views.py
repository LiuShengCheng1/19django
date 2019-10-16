from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book = Book(name='西游记', author='吴承恩', prize=88)
    book.save()
    return HttpResponse('豆瓣图书')
