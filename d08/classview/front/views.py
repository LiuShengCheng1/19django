from django.shortcuts import render
from django.views.decorators.http import require_GET, require_safe, require_POST, require_http_methods
from .models import Article
from django.http import HttpResponse
from django.views.generic import View, TemplateView,ListView
from django.core.paginator import Paginator,Page

@require_GET
def add_article(request):
    articles = []
    for x in range(0, 200):
        article = Article(title="标题：%s" % x, content="内容：%s" % x)
        articles.append(article)
    Article.objects.bulk_create(articles)

    return HttpResponse("文章添加成功")


class AddArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_article.html')

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get('name')
        book_content = request.POST.get('content')
        print("name:{},content:{}".format(book_name, book_content))
        return HttpResponse("success")


class ArticleDetail(View):
    def get(self, request, article_id):
        print("文章的ID是：%s" % article_id)
        return HttpResponse("success")

    def dispatch(self, request, *args, **kwargs):
        print("不管什么请求都走这里")
        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)

    # 上面只允许get请求  其他请求都会给反馈不支持
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持get之外的请求")


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['name'] = 'sdfsdhfkhs'
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView,self).get_context_data()
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator,page_obj,3)
        context.update(pagination_data)
        return context
    
    def get_pagination_data(self,paginator,page_obj,around_count=3):
        # 获取当前页码
        current_page = page_obj.number
        num_pages = paginator.num_pages    # 计算总页数

        left_has_more = False
        right_has_more = False

