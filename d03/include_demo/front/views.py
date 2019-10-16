from django.shortcuts import render


def index(request):
    context = {
        'username':'徐凤年'
    }
    return render(request,'index.html',context=context)

def company(request):
    return render(request,'company.html')


def school(request):
    return render(request,'school.html')