from django.http import HttpResponse


def article(request):
    return HttpResponse("文章首页")

def article_list_month(request,month):
    text = "您要查找的"