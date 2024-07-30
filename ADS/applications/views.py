from django.shortcuts import render

def list_applications(request):
    return render(request, 'applications/list_applications.html')

def application(request):
    return render(request, 'applications/application.html')