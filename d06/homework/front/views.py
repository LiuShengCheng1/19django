from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Course,Score,Teacher
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
from django.db import connection
# Create your views here.

def index(request):
    rows = Student.objects.annotate(avg=Avg("score__number")).filter(avg__gte=60).values("id","avg")
    for row in rows:
        print(row)
    print(connection.queries)
    return HttpResponse("index")


def index1(request):
    rows = Student.objects.annotate(course_nums=Count("score__course"), total_score=Sum("score__number"))\
        .values("id", "name", "course_nums", "total_score")
    for row in rows:
        print(row)
    print(connection.queries)
    return HttpResponse("index1")


def index2(request):
    nums = Teacher.objects.filter(name__startswith="李").count()
    print(nums)
    return HttpResponse("index2")


def index3(request):
    rows = Student.objects.annotate(nums=Count("score__course", filter=Q(score__course__teacher__name='黄老师'))).filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
    for row in rows:
        print(row)
    return HttpResponse("index3")

def index4(request):
    nums = Student.objects.filter(Q(score__course=1) & Q(score__course=2)).values("id","name")
    # nums = Student.objects.filter(score__course__in=[1,2]).distinct().values('id','name')
    for num in nums:
        print(num)
    return HttpResponse("index4")

def index5(request):
    rows = Student.objects.annotate(nums=Count("score__course", filter=Q(score__course__teacher__name='黄老师')))\
        .filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
    for row in rows:
        print(row)
    return HttpResponse("index5")

def index6(request):
    nums = Student.objects.exclude(score__gte=60)
    for num in nums:
        print(num)
    return HttpResponse("index6")


def index7(request):
