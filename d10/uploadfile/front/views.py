from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        myfile = request.FILES.get('mylile')

        with open('somefile.jpg','wb') as fp:
            for chunk in myfile.chunks():
                fp.write(chunk)

            return HttpResponse('success')