from datetime import datetime
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

class Articles(models.Model):
    title = models.CharField('ФИО заявителя', max_length=50)
    phone_number = PhoneNumberField('Номер телефона')
    full_text = models.TextField('Текст заявки')
    date = models.DateTimeField('Дата/время', default=datetime.now())
    street = models.CharField('Улица', max_length=50, null=True)
    house = models.CharField('Дом', max_length=3, null=True)
    flat = models.CharField('Квартира', max_length=3, null=True)
    materials = models.CharField('Материалы', max_length=50, null=True)
    executor = models.CharField('Исполнитель', max_length=50, null=True)
    comment = models.CharField('Комментарий', max_length=50, null=True)
    
    
    def get_absolute_url(self):
        return reverse('list_of_request:application', kwargs={"application_id": self.pk})
    
    def __str__(self):
        return self.full_text
    
    class Meta:
        db_table = 'applications'
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        ordering = ("id",)
    
    # "{% url "list_of_request:application" c.pk %}"
    
    
    
    
    

    
    

    
    
    
    
    
    
    
    

        
