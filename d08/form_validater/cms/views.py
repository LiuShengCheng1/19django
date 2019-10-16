from django.shortcuts import render
from django.views.generic import  View
from .forms import MyForm
# Create your views here.


class IndexView(View):
    def get(self,request):
        form = MyForm()
        return render(request)
