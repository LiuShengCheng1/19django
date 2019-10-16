from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum
from django.db import connection
# Create your views here.

# 获取所有图书的定价的评价
def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # aggregate 要通过connection查看最终执行的sql语句
    print(connection.queries)
    return HttpResponse("index")

