# Generated by Django 5.0.7 on 2024-07-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_alter_list_of_applications_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_of_applications',
            name='FIO',
            field=models.TextField(max_length=250, verbose_name='ФИО заявителя'),
        ),
        migrations.AlterField(
            model_name='list_of_applications',
            name='text',
            field=models.TextField(max_length=500, verbose_name='текст заявки'),
        ),
    ]
