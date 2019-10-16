from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render


def index(request):
    # 第二种方式导入
    # html = render_to_string('index.html')
    #
    # return HttpResponse(html)
    # 第三种方式导入
    return render(request, 'index.html')
