from django.http import HttpResponse
import json


def index(request):
    response = HttpResponse('<h1>前锋课堂</h1>',content_type='text/plain;charset=utf-8')
    # response = HttpResponse('<h1>前锋课堂</h1>')
    response.status_code =400
    response['X-Token'] = '1000phone'
    return response

def json_view(request):
    person = [
        {
            'username':'sdfdg',
            'password':'123321',
            'age':'18'
        }
    ]

    person_str = json.dumps(person)
    response = HttpResponse(person_str,content_type='application/json')
    return response


def template_csv_view(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment"