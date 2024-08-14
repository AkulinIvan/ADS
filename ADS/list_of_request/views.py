from django.shortcuts import render
from django.core.paginator import Paginator
from .models import  Articles
from .forms import ArticlesForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def list_of_applications(request):
    page = request.GET.get('page', 1)
    content = Articles.objects.all()
    paginator = Paginator(content, 3)
    current_page = paginator.page(int(page))
    context = {
        "title": "Список заявок",
        "content": current_page,
    }
    return render(request, 'list_of_request/list_of_applications.html', context)
    
    
    
# @login_required
def application_detail(request, application_id):
    application = Articles.objects.get(pk=application_id)
    content = { 
        'title': 'Детали заявки',
        'application': application
    }
    return render(request, 'list_of_request/application_detail.html', content)


def create_application(request):
    error = ''
    if request.method=="POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_of_request:applications'))
        else:
            error = 'Форма была не верной'
    
    form = ArticlesForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'list_of_request/create_application.html', data)
    # if request.method == 'POST':
    #     form = ApplicationForm(request.POST)
        
    #     if form.is_valid():
    #         #print(form.cleaned_data)
    #         feed = Application(
    #             status = form.cleaned_data['status'], 
    #             priority = form.cleaned_data['priority'], 
    #             street = form.cleaned_data['street'],
    #             house = form.cleaned_data['house'],
    #             flat = form.cleaned_data['flat'],
    #             text = form.cleaned_data['text'],
    #             comment = form.cleaned_data['comment'],
    #             materials = form.cleaned_data['materials'],
    #             name = form.cleaned_data['name'],
    #             executor = form.cleaned_data['executor'],
    #         )
    #         feed.save()
            
            
    #         return HttpResponseRedirect('applications')
        
    # else:
    #     form = ApplicationForm()
    
    # return render(request, 'list_of_request/create_application.html', context={
    #     'form': form
    # })





