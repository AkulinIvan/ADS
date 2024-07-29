from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'title': 'АДС',
        'content': 'Главная страница аварийно-диспетчерской службы',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('Страница о нас')
