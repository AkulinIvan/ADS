from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField

class User(User):
    
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self) -> str:
        return self.username
    

# class Executor(models.Model):
#     name = models.CharField(max_length=150, unique=True, verbose_name='Исполнитель')
#     phone_number = PhoneNumberField("Телефон")
#     e_mail = models.EmailField('E-mail')
#     role = models.CharField('Роль', max_length=50)
#     company = models.CharField('Управляющая компания', max_length=50)
#     id_ATS = models.CharField('Номер АТС', max_length=50)
#     sms = models.CharField("Вид смс", max_length=50)
#     login = models.CharField("Логин", max_length=50)
#     password = models.CharField("Пароль", max_length=50)