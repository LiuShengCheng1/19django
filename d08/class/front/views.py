from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST,require_safe,require_http_methods
from .models import Article
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView
# Create your views here.

@require_GET
def add_article(request):
    articles = []
    for x in range(0,200):
        article = Article(title="标题：%s" % x, content="内容：%s"% x)
        articles.append(article)
    # bulk_create 数据批量插入
    Article.objects.bulk_create(articles)
    return HttpResponse("文章添加成功")


class AddArticleView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_article.html')

    def post(self,request,*args,**kwargs):
        book_name = request.POST.get('name')
        book_content = request.POST.get('content')
        print("name:{},content:{}".format(book_name,book_content))
        return HttpResponse("success")

class ArticleDetail(View):
    def get(self,request,article_id):
        print("文章id是：%s" % article_id)
        return HttpResponse("success")
    def dispatch(self, request, *args, **kwargs):
        print("不管什么方式请求都从这边走")
        # 重写super方法
        return super(ArticleDetail,self).dispatch()
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持get之外的其他请求")

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_content_data(self,**kwargs):
        context = super(HomeView,self).get_context_data()
        context['name'] = '飞雪连天射白鹿'
        return context

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'article'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(AddArticleView,self).get_context_data
        return context




