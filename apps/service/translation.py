from modeltranslation.translator import register, TranslationOptions
from .models import ContactInfo


@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('title',)  # Fields to translate

