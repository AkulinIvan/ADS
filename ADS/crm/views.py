from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm, AssignForm

def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.resident = request.user.resident  # Убедитесь, что у пользователя есть профиль Resident
            application.save()
            return redirect('application_list')
    else:
        form = ApplicationForm()
    return render(request, 'crm/create_application.html', {'form': form})

def assign_application(request, application_id):
    application = Application.objects.get(id=application_id)
    if request.method == 'POST':
        form = AssignForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_detail', application_id=application.id)
    else:
        form = AssignForm(instance=application)
    return render(request, 'crm/assign_application.html', {'form': form, 'application': application})
