from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.


def index(request):
    # user = User.objects.create_user(username="kangbazi",email="kangbazi@163.com",password="123456")
    # user = User.objects.create_superuser(username="superman1",email="superman1@163.com",password="123456")
    # user.last_name = '666'
    # user.first_name = 'kangbazi'
    # user = User.objects.get(pk=2)
    # user.set_password('112233')
    # user.save()

    username =
    return render(request,'index.html')