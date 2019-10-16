from django.shortcuts import render
from django.http import HttpResponse
from frontuser.models import FrontUser
from article.models import Article


def ont_to_many_view(request):
    article = Article(title="钢铁是怎样炼成的",content="士大夫十分后和")
    users = FrontUser(username="dfsh")

    users.save()
    article.author = users
    article.save()
    return HttpResponse()