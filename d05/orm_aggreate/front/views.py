from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Sum
from django.db import connection
# Create your views here.
# 获取所有图书的定价的平均价格


def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    print(connection.queries)
    return HttpResponse("index")


# 每一本销售书籍的平均价格
def index1(request):
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    result = Book.objects.annotate(avg=Avg("bookorder__price"))
    # print(result)
    for res in result:
        print('%s%s' % (res.name,res.avg))
    print(connection.queries)
    return HttpResponse("index")


# 查看总共有多少本书
def index2(request):
    # book表中总共多少书
    result = Book.objects.annotate(booksales=Count("bookorder"))
    for res in result:
        print("%s%s" %(res.name,res.booksales))
    print(connection.queries)
    return HttpResponse("index2")


def index5(request):
    result = BookOrder.objects.annotate(booksum=Sum("bookorder__price"))
    for res in result:
        print("%s%s" %(res.name,res.Sum))
    return HttpResponse("index5")