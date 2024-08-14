from django import forms
from django.forms import ModelForm
from .models import Articles
from phonenumber_field.modelfields import PhoneNumberField

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'phone_number', 'full_text', 'date', 'street', 'house', 'flat', 'materials', 'executor', 'comment']
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО заявителя'
            }),
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "full_text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заявки'
            }),
            "date": forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время публикации'
            }),
            "street": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Улица'
            }),
            "house": forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дом'
            }),
            "flat": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Квартира'
            }),
            "materials": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Материалы'
            }),
            "executor": forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Исполнитель'
            }),
            "executor": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Исполнитель'
            }),
            "comment": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
        }


