from django.shortcuts import render


def index(request):
    # context = {
    #     'age': 20
    # }
    context = {
        'hero': [
            '剑圣',
            '酒桶',
            '寒冰'
        ]
    }

    return render(request, 'index.html', context=context)
