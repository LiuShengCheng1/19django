from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.views.decorators.http import require_POST,require_http_methods
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from utils import restful
User = get_user_model()
@require_POST
def register(request):
    form =RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = User.objects.create_user(telephone=telephone,username=username,password=password)
        login(request,user)
        return restful.success()
    else:
        errors = form.get_errors()
        print(errors)
        return restful.params_error(message=errors)


@require_http_methods(['GET','POST'])
def login_view(request):
    # 实例化表单对象
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful
            else:
                return restful.unauth_error(message="您的账户被冻结")
        else:
            return restful.params_error(message="手机号或者密码错误")
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)