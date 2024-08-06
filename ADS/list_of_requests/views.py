from django.shortcuts import render

def list_of_requests(request):
    context={
        'title': 'АДС - Заявки',
        'content': 'Здесь будет таблица заявок'
        
    }
    return render(request, 'list_of_requests/requests.html', context)

def new_request(request):
    context={
        'title': 'АДС - Новая заявка',
        'content': 'Здесь форма новой заявки'
        
    }
    return render(request, 'list_of_requests/new_request.html', context)



