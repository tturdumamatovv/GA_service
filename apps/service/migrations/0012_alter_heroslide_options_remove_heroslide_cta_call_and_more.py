# Generated by Django 5.1.1 on 2024-09-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_remove_heroslide_google_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heroslide',
            options={'verbose_name': 'Слайд на главной странице', 'verbose_name_plural': 'Слайды на главной странице'},
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='cta_call',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='cta_whatsapp',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='description',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='rating_and_reviews',
        ),
        migrations.RemoveField(
            model_name='heroslide',
            name='slide_type',
        ),
        migrations.AddField(
            model_name='heroslide',
            name='best_in_town_text',
            field=models.CharField(blank=True, help_text='Текст вроде "Best in town Computer and Mobile Phone Repair Shop"', max_length=255, null=True, verbose_name='Лучший в городе текст'),
        ),
        migrations.AddField(
            model_name='heroslide',
            name='call_link',
            field=models.CharField(blank=True, help_text='Введите номер телефона в формате tel:+971585929333', max_length=255, null=True, verbose_name='Ссылка для звонка'),
        ),
        migrations.AddField(
            model_name='heroslide',
            name='call_text',
            field=models.CharField(blank=True, default='Call Now', max_length=100, null=True, verbose_name='Текст для Call кнопки'),
        ),
        migrations.AddField(
            model_name='heroslide',
            name='rating_text',
            field=models.CharField(blank=True, help_text='Например, "Rated 4.9 with 34 reviews"', max_length=255, null=True, verbose_name='Текст рейтинга'),
        ),
        migrations.AddField(
            model_name='heroslide',
            name='whatsapp_link',
            field=models.CharField(blank=True, help_text='Введите ссылку WhatsApp, например, https://wa.me/971585929333', max_length=255, null=True, verbose_name='Ссылка на WhatsApp'),
        ),
        migrations.AddField(
            model_name='heroslide',
            name='whatsapp_text',
            field=models.CharField(blank=True, default='WhatsApp Now', max_length=100, null=True, verbose_name='Текст для WhatsApp кнопки'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение для слайда', null=True, upload_to='hero_slider/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='subtitle1',
            field=models.CharField(blank=True, help_text='Первый подзаголовок, например, "Premium out-of-warranty Apple Service Center in Dubai"', max_length=255, null=True, verbose_name='Подзаголовок 1'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='subtitle2',
            field=models.CharField(blank=True, help_text='Второй подзаголовок, например, "Visit our service center to avail repair services..."', max_length=255, null=True, verbose_name='Подзаголовок 2'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='title',
            field=models.CharField(blank=True, help_text='Основной заголовок для слайда, например, "Professional Repair Services..."', max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='heroslide',
            name='video',
            field=models.FileField(blank=True, help_text='Загрузите видео для слайда (по желанию)', null=True, upload_to='hero_slider/videos/', verbose_name='Видео'),
        ),
    ]
