from django.urls import path
from list_of_request import views


app_name = 'list_of_request'

urlpatterns = [
    path('', views.list_of_applications, name='applications'),
    path('<int:page>/', views.list_of_applications, name='applications'),
    path('application/<int:application_id>/', views.application_detail, name='application'),
    path('create/', views.create_application, name='create_application'),
]