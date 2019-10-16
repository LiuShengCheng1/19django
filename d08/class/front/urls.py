from django.urls import path
from . import views

# 应用命名空间，多个app之间，有可能产生同名的url。
# 这时候为了避免反转url的时候产生混淆，可以使用应用命名空间，来做区分
app_name = 'front'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_article/', views.AddArticleView.as_view(), name='add_article'),
    path('add_detail/<article_id>/', views.ArticleDetail.as_view(), name='article_detail'),
    # path('add_detail/<article_id>/', views.ArticleDetail.as_view(), name='article_detail'),

]
