from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(TranslationAdmin):
    list_display = ('title', 'phone_number')
