from django.shortcuts import render,redirect,reverse
from .models import User
from .forms import SingUpForm,SingInForm
from django.views.generic import View
from django.contrib import messages


def index(request):
    users = User.objects.all()
    for user in users:
        print(user.msername)
    return render(request,'index.html',context={"username":user.usename})

class SingUpView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        form = SingUpForm(request.Post)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # telephone = form.cleaned_data.get('telephone')
            # print(username,telephone)
            form.save()
            return redirect(reverse('index'))
        else:
            # {"telephone":[]}
            print(form.errors.get_json.data())
            return redirect(reverse('signup'))

class SignInView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        form = SingInForm(request.Post)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info()
