# Generated by Django 5.1.1 on 2024-09-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0044_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='footersection',
            name='title_work_time',
            field=models.CharField(blank=True, null=True, verbose_name="Заголовок 'Время работы'"),
        ),
    ]
