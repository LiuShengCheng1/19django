from django.shortcuts import render
from datetime import datetime


# Create your views here.

def index(request):
    context = {
        'value': '展昭',
        'mytime': datetime(year=2019, month=9, day=19)
    }
    return render(request, 'index.html', context=context)
