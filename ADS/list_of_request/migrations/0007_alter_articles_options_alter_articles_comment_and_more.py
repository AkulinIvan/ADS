# Generated by Django 5.0.7 on 2024-08-14 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_request', '0006_alter_articles_comment_alter_articles_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('id',), 'verbose_name': 'Заявку', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='comment',
            field=models.CharField(max_length=50, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 14, 7, 43, 21, 319229), verbose_name='Дата/время'),
        ),
        migrations.AlterModelTable(
            name='articles',
            table='applications',
        ),
    ]
