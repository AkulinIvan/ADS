from django.urls import path
from list_of_requests import views


app_name = 'list_of_requests'

urlpatterns = [
    path('', views.list_of_requests, name='requests'),
    path('new_request', views.new_request, name='new_request'),
]