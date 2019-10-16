from django.http import HttpResponse,StreamingHttpResponse
from django.template import loader
import csv


def index(request):
    # 声明这是一个csv文件
    response = HttpResponse(content_type="text/csv")
    # 添加head头
    # attachment声明文件为附件，作为附件下载
    response['Content-Disposition'] = "attachment;filename=1902.csv"
    # 使用csv文件的writer方法，将相应的数据写入到response中
    writer = csv.writer(response)
    writer.writerow(['username', 'age', 'height'])   # 设置表头
    writer.writerow(['chenpingan', '18','178cm'])    # 数据行
    return response


def template_csv_view(request):
    # 声明文件类型
    response = HttpResponse(content_type="text/csv")
    # 声明文件干事
    response['Content-Disposition'] = "attachment;filename=1902.csv"
    context = {
        'rows':[
            ['username','age'],
            ['kangbazi','19'],
            ['adfdg','29'],
            ['fgdfg','34']
        ]
    }

    template = loader.get_template('abc.html')
    csv_template = template.render(context)
    response.content = csv_template
    return response



