from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    response = HttpResponse("index首页")
    expires = datetime(year=2019,month=10,day=1,minute=0,second=0)
    # response.set_cookie('user_id','abc123456',max_age=180)
    response.set_cookie('user_id','abc123456',max_age=180)
    return response


def del_cookie(request):
    response = HttpResponse('delete_cookie')
    response.delete_cookie('user_id')
    return response

def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)


def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)



