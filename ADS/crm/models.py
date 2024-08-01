from django.db import models
from django.contrib.auth.models import User

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class Application(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    text = models.TextField()
    comment = models.TextField()
    

class Notification(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
