from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        form = MessageBoardForm()
        return render(request,'index.html',context={"form":form}) #将表单渲染到模板上

    def post(self,request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():  # 判断是否符合要求
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")