from django.shortcuts import render
import uuid
from rest_framework import viewsets,status
from rest_framework.exceptions import APIException,NotFound
from rest_framework.response import Response
from .models import Book, Game,Movie,User
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from App.serializers import(
     MovieSerializers,
     BookSerializers,
     Book1Serializers,
     Book2Serializers,
     GameSerializers,
     UserSerializers,
)
from django.core.cache import cache     # 导入缓存


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book2Serializers


# 仅仅只能用来新增创建数据，即post请求
# class GameViewSet(CreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers


# 仅仅只能用来查看数据，即GET请求
# class GameViewSet(ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers


# 查看和新增数据都可以，get和post请求,其他都不允许
class GameViewSet(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class UserViewSet(CreateAPIView):
    serializer_class = UserSerializers
    def post(self,request,*args,**kwargs):
        action = request.query_params.get('action')
        if action == 'register':
            return self.create(request,*args,**kwargs)
        elif action == 'login':
            return self.do_login(request,*args,**kwargs)
        else:
            raise APIException(detail="请提供正确的操作")

    def do_login(self,request,*args,**kwargs):
        u_name = request.data.get('u_name')
        u_password = request.data.get('u_password')

        try:
            user = User.objects.filter(u_name=u_name).first()
        except User.DoesNotExist as e:
            raise NotFound(detail="该用户不存在")

        if user.u_password != u_password:
            raise APIException(detail="密码错误")

        token = uuid.uuid4().hex

        cache.set(token,user.id,timeout=60*60*24*7)

        data = {
            "status": status.HTTP_200_OK,
            "message": "登录成功",
            "token": token
        }

        return Response(data)