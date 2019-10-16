from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    # book = Book(name="西游记",author="吴承恩",price=188)
    # book.save()
    # book = Book(name="水浒传",author="施耐庵",price=127)
    # book.save()

    #查询
    # book = Book.objects.get(pk=1)
    # print(book)
    # book = Book.objects.filter(name="西游记")
    # print(book)
    #删除
    # book = Book.objects.get(pk=2)
    # book.delete()
    #更新
    book = Book.objects.get(pk=1)
    book.price = 300
    book.save()
    return HttpResponse("豆瓣图书")