from django.shortcuts import render


def index(request):
    context = {
        'books': [
            '水浒传',
            '三国演义',
            '茶花女',
            '西游记',
        ],
        'persons': {
            'username': '李时珍',
            'work': 'doctor',
            'country': '明',
        },
        'movies': [
            {
                'name': '钢铁侠',
                'author': '托利萨塔克'
            },
            {
                'name':'黑寡妇',
                'author':'adgdfg'
            },
            {
                'name':'战狼2',
                'author':'吴京'
            }
        ]
    }
    return render(request, 'index.html', context=context)
