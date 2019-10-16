from django.shortcuts import render
from datetime import datetime


def greet(word):
    return "hello word %s" % word


def index(request):
    context = {
        'greet': greet
    }
    return render(request, 'index.html', context=context)


def add_view(request):
    context = {
        'value1': ['1', '2', '3', '4'],
        'value2': ['5', '6', 7]
    }
    return render(request, 'add.html', context=context)


def cut_view(request):
    return render(request, 'cut.html')


def date_view(request):
    context = {
        'birthday': datetime.now()
    }
    return render(request, 'date.html', context=context)


def first_view(request):
    context = {
        'value': "abc"
    }
    return render(request, 'first.html', context=context)

def last_view(request):
    context = {
        'value': "abc"
    }
    return render(request, 'last.html', context=context)


def floatformat_view(request):
    context = {
        'value':345.118
    }
    return render(request,'floatformat.html',context=context)


def join_view(request):
    context = {
        'value':['a','love','bv']}
    return render(request,'join.html',context=context)

def length_view(request):
    context = {
        'value':'abcdefg'}
    return render(request,'length.html',context=context)

def upper_view(request):
    context = {
        'value':'abcdefg'}
    return render(request,'upper.html',context=context)