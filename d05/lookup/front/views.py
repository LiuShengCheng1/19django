from django.shortcuts import render
from .models import Article,Category
# Create your views here.
def index(request):
    Article(title="心有猛虎",content="细嗅蔷薇")

    category = Category(name="道心")
    category.save()
    article.category = category
    article.save()