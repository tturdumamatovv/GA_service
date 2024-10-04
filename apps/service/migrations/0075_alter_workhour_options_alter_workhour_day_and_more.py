# Generated by Django 5.1.1 on 2024-10-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0074_footersection_call_footersection_whatsapp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workhour',
            options={'ordering': ['day'], 'verbose_name': 'Рабочее время', 'verbose_name_plural': 'Рабочее время'},
        ),
        migrations.AlterField(
            model_name='workhour',
            name='day',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='workhour',
            name='day_en',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], null=True, verbose_name='День'),
        ),
        migrations.AlterField(
            model_name='workhour',
            name='day_ru',
            field=models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота'), (7, 'Воскресенье')], null=True, verbose_name='День'),
        ),
    ]
