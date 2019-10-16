from django.http import HttpResponse


def book(request):
    return HttpResponse("豆瓣图书")


def movie(request):
    return HttpResponse("豆瓣电影")


def book_detail(request, book_id, category_id):
    text = "您获取的图书ID是%s,图书分类是%s" % (book_id, category_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET['id']
    username_id = request.GET['username']
    text = "作者的id是%s,名字是%s" % (author_id, username_id)
    return HttpResponse(text)
