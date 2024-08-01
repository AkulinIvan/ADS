from django.urls import path
from crm import views

app_name = 'crm'

urlpatterns = [
    path('application/create/', views.create_application, name='create_application'),
    path('application/assign/', views.assign_application, name='assign_application'),
]