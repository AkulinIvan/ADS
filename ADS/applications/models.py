from django.db import models
from django.contrib.auth.models import User

class List_of_applications(models.Model):
    CURRENT = 'Текущая'
    COMMERCIAL = 'Коммерческая'
    EMERGENCY = 'Аварийная'
    PLANNED = 'Плановая'
    DUTY = 'Дежурная'
    
    
    CHOICES_PRIORITY = (
        (CURRENT, 'Текущая'),
        (COMMERCIAL, 'Коммерческая'),
        (EMERGENCY, 'Аварийная'),
        (PLANNED, 'Плановая'),
        (DUTY, 'Дежурная')
        
    )
    
    created_by = models.DateTimeField('Дата/время', auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    street = models.CharField('Улица', max_length=50)
    house = models.CharField('дом', max_length=50)
    flat = models.CharField('квартира', max_length=50)
    text = models.TextField('текст заявки', max_length=500)
    period_of_execution = models.CharField('срок исполнения', max_length=50)
    FIO = models.TextField('ФИО заявителя', max_length=250)
    telephone_number = models.CharField('телефон', max_length=50)
    
    #created_at = models.ForeignKey(User, related_name='application')
    priority = models.CharField('Приоритет', max_length=12, choices=CHOICES_PRIORITY, default = CURRENT)
    
    def __str__(self):
        return self.FIO
    
    
    
