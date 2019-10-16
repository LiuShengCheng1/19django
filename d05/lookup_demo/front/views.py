from django.shortcuts import render
from .models import Article, Category
from django.http import HttpResponse


# Create your views here.

def index(request):
    article = Article(title="心有猛虎", content="细嗅蔷薇")

    category = Category(name="诗歌")
    category.save()
    article.category = category
    article.save()
    return HttpResponse("添加成功")


def index1(request):
    # 只能是filter才能查看query
    article = Article.objects.filter(title__exact="hello")
    print(article.query)
    return HttpResponse("index1")


def index2(request):
    article = Article.objects.filter(title__contains='he')
    print(article.query)
    print(article)
    return HttpResponse("index2")


def index3(request):
    article = Article.objects.filter(title__icontains='hello')
    print(article.query)
    print(article)
    return HttpResponse('index3')


def index4(request):
    # articles = Article.objects.filter(id__in=[1,3])
    # for article in articles:
    #     print(article)
    # return HttpResponse('index4')

    article = Article.objects.filter(title__icontains="hello")
    categories = Category.objects.filter(article__in=article)
    for category in categories:
        print(category)
    print(categories.query)
    return HttpResponse('index4')
