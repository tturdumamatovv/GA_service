# Generated by Django 5.1.1 on 2024-10-04 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0076_alter_workhour_options_alter_workhour_day_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workhour',
            name='day_en',
        ),
        migrations.RemoveField(
            model_name='workhour',
            name='day_ru',
        ),
    ]
