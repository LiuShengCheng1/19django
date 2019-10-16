from django.shortcuts import render


class Person(object):
    def __init__(self, username):
        self.username = username


def index(request):
    # p = Person('赵云')
    context = {
        'person': {
            'username': 'kangbazi',
            'age': 78
        }
    }
    return render(request, 'index.html', context=context)
