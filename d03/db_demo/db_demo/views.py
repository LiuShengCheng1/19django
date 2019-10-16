from django.shortcuts import render
from django.db import connection


def index(request):
    #创建连接实例
    cursor = connection.cursor()
    cursor.execute("select * from users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,'index.html')