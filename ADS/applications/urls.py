from django.urls import path
from applications import views


app_name = 'applications'

urlpatterns = [
    path('', views.list_applications, name='index'),
    path('application/', views.application, name='application'),
]