from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactInfo(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название')
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Номер телефона')
    )

    class Meta:
        verbose_name = _('Контактная информация')
        verbose_name_plural = _('Контактные информации')

    def __str__(self):
        return self.title
