from django.http import HttpResponse, JsonResponse
import json


def index(request):
    # response = HttpResponse("<h1>长生诀</h1>")
    response = HttpResponse("<h1>长生诀</h1>", content_type="text/plain;charset=utf-8")
    # content_type 参数：
    # 1、text/plain -->纯文本
    # 2、text/html --> 默认为html文件
    # 3、text/css --> css文件
    # 4、text/javascript -->js文件
    # 5、multipart/form-data --> 文件提交
    # 6、application/json -->json传输
    # 7、application/xml --> xml文件
    response.status_code = 400  # 状态码
    response['X-Token'] = '1000phone'  # 设置请求头
    return response


def json_view(request):
    person = [
        {
            'username': '陈平安',
            'work': '武夫',
            'age': '18'
        },
        {
            'username': '宁姚',
            'work': '剑仙',
            'age': '17'
        }
    ]
    # 原始写法，将content_type 参数定义为application/json
    # person_str = json.dumps(person)     dumps（序列化）只能用于字典，非字典需要添加safe=False
    # response = HttpResponse(person_str,content_type="application/json")
    # return response
    response = JsonResponse(person,safe=False)
    return response
