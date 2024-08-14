# Generated by Django 5.0.7 on 2024-08-13 01:24

import datetime
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='ФИО заявителя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('full_text', models.TextField(verbose_name='Текст заявки')),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 8, 13, 8, 24, 1, 187166), verbose_name='Дата/время')),
                ('street', models.CharField(max_length=50, null=True, verbose_name='Улица')),
                ('house', models.CharField(max_length=3, null=True, verbose_name='Дом')),
                ('flat', models.CharField(max_length=3, null=True, verbose_name='Квартира')),
                ('materials', models.CharField(max_length=50, null=True, verbose_name='Материалы')),
                ('executor', models.CharField(max_length=50, null=True, verbose_name='Исполнитель')),
            ],
        ),
    ]