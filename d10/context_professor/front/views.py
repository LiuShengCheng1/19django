from django.shortcuts import render
from .models import User
# Create your views here.


def index(request):
    users = User.objects.all()
    for user in users:
        print(user)
    return render('request','index.html',context={"username":user.username})