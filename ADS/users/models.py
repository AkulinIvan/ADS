from django.db import models
from django.contrib.auth.models import User

class User(User):
    
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self) -> str:
        return self.username