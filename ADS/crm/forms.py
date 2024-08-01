from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone_number', 'description', 'status', 'street', 'house', 'comment', 'text']
        

class AssignForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['assigned_to']