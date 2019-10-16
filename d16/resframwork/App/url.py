from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from App import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    # path(r'game/',views.GameViewSet.as_view())
    url(r'^game/', views.GameViewSet.as_view(), name='game'),
    url(r'^movie/$', views.MovieViewSet.as_view(
        actions={
            "get": "list",
            "post": "create",
        }
    ), name='movie'),  # 上面只能增加或者查看所有，不能根据id查看某一个
    url(r'^movie/(?P<pk>\d+)/',views.MovieViewSet.as_view(
        actions ={
            "get":"retrieve",
            "put":"update",
            "patch":"partial_update",
            'delete':'destroy'
        }
    ),name='movies'),         # 根据id查看更新以及删除
    url(r'^users/',views.UserViewSet.as_view(),name='users')
]
