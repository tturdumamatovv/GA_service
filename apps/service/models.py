from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    class Meta:
        abstract = True  # This makes it an abstract base class

    def save(self, *args, **kwargs):
        # If there's already an instance, prevent saving another one
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(_('Only one instance of this model is allowed.'))
        return super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ContactInfo(SingletonModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название')
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_('Номер телефона')
    )
    phone_link = models.CharField(
        max_length=30,
        verbose_name=_('Телефонная ссылка'),
        help_text=_('Введите номер в формате: +971XXXXXXX'),
        blank=True, null=True
    )
    opening_time_title = models.CharField(
        max_length=100,
        verbose_name=_('Заголовок время открытия'),
        help_text=_('Например: Время открытия'),
        blank=True, null=True
    )
    opening_days = models.CharField(
        max_length=100,
        verbose_name=_('Дни работы'),
        help_text=_('Например: пн-сб: 10:00–20:00 вс: ЗАКРЫТО'),
        blank=True, null=True
    )

    class Meta:
        verbose_name = _('Контактная информация')
        verbose_name_plural = _('Контактные информации')

    def __str__(self):
        return self.title


class NavigationLink(SingletonModel):
    home = models.CharField(
        max_length=100,
        verbose_name=_('Главная'),
        default="Главная"
    )
    services = models.CharField(
        max_length=100,
        verbose_name=_('Услуги'),
        default="Услуги"
    )
    about_us = models.CharField(
        max_length=100,
        verbose_name=_('О нас'),
        default="О нас"
    )
    contacts = models.CharField(
        max_length=100,
        verbose_name=_('Контакты'),
        default="Контакты"
    )

    class Meta:
        verbose_name = _('Навигационная ссылка')
        verbose_name_plural = _('Навигационные ссылки')

    def __str__(self):
        return self.home


class HeroSlide(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Заголовок'),
        help_text=_('Основной заголовок для слайда, например, "Professional Repair Services..."'),
        blank=True,
        null=True
    )
    subtitle1 = models.CharField(
        max_length=255,
        verbose_name=_('Подзаголовок 1'),
        help_text=_('Первый подзаголовок, например, "Premium out-of-warranty Apple Service Center in Dubai"'),
        blank=True,
        null=True
    )
    subtitle2 = models.CharField(
        max_length=255,
        verbose_name=_('Подзаголовок 2'),
        help_text=_('Второй подзаголовок, например, "Visit our service center to avail repair services..."'),
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='hero_slider/',
        verbose_name=_('Изображение'),
        help_text=_('Загрузите изображение для слайда'),
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='hero_slider/videos/',
        verbose_name=_('Видео'),
        blank=True,
        null=True,
        help_text=_('Загрузите видео для слайда (по желанию)')
    )

    # Fields for WhatsApp and Call buttons
    whatsapp_text = models.CharField(
        max_length=100,
        verbose_name=_('Текст для WhatsApp кнопки'),
        blank=True,
        null=True
    )
    whatsapp_link = models.CharField(
        max_length=255,
        verbose_name=_('Ссылка на WhatsApp'),
        help_text=_('Введите ссылку WhatsApp, например, https://wa.me/971585929333'),
        blank=True,
        null=True
    )
    call_text = models.CharField(
        max_length=100,
        verbose_name=_('Текст для Call кнопки'),
        blank=True,
        null=True
    )
    call_link = models.CharField(
        max_length=255,
        verbose_name=_('Ссылка для звонка'),
        help_text=_('Введите номер телефона в формате tel:+971585929333'),
        blank=True,
        null=True
    )

    # Fields for the rating and description
    best_in_town_text = models.CharField(
        max_length=255,
        verbose_name=_('Лучший в городе текст'),
        help_text=_('Текст вроде "Best in town Computer and Mobile Phone Repair Shop"'),
        blank=True,
        null=True
    )
    rating_text = models.CharField(
        max_length=255,
        verbose_name=_('Текст рейтинга'),
        help_text=_('Например, "Rated 4.9 with 34 reviews"'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Слайд на главной странице')
        verbose_name_plural = _('Слайды на главной странице')

    def __str__(self):
        return self.title


class AdvantageIconText(models.Model):
    hero_slide = models.ForeignKey(
        HeroSlide,
        related_name='advantages',
        on_delete=models.CASCADE,
        verbose_name=_('Слайд'),
        help_text=_('Слайд, к которому относится данное преимущество')
    )
    icon = models.FileField(
        upload_to='advantage_icons/',
        verbose_name=_('Иконка'),
        help_text=_('Загрузите SVG или PNG файл для иконки')
    )
    text = models.CharField(
        max_length=255,
        verbose_name=_('Текст преимущества'),
        help_text=_('Текст преимущества, например, "Professional team"')
    )

    class Meta:
        verbose_name = _('Преимущество')
        verbose_name_plural = _('Преимущества')

    def __str__(self):
        return self.text


class FeaturesSection(SingletonModel):
    title = models.CharField(
        max_length=255,
        verbose_name=_('Заголовок секции'),
        help_text=_('Заголовок, который отображается над сеткой с изображениями')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Раздел техника')
        verbose_name_plural = _('Раздел техники')


class FeatureItem(models.Model):
    section = models.ForeignKey(
        FeaturesSection,
        on_delete=models.CASCADE,
        related_name='feature_items',
        verbose_name=_('Секция')
    )
    image = models.ImageField(
        upload_to='features_images/',
        verbose_name=_('Изображение'),
        help_text=_('Загрузите изображение для элемента')
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название элемента'),
        help_text=_('Название, отображаемое под изображением')
    )
    link = models.URLField(
        verbose_name=_('Ссылка для элемента'),
        help_text=_('URL для ссылки, которая будет прикреплена к элементу')
    )

    def __str__(self):
        return self.title


class ServicesSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Раздел услуга')
        verbose_name_plural = _('Раздел услуги')


class ServiceTab(models.Model):
    section = models.ForeignKey(ServicesSection, on_delete=models.CASCADE, related_name="tabs", verbose_name=_("Секция"))
    title = models.CharField(max_length=255, verbose_name=_("Заголовок таба"))
    tab_id = models.CharField(max_length=100, verbose_name=_("ID таба (для переключения)"))
    is_active = models.BooleanField(default=False, verbose_name=_("Активный по умолчанию"))
    image = models.ImageField(upload_to="service_images/", verbose_name=_("Изображение таба"), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Кнопка для услуги')
        verbose_name_plural = _('Кнопки для услуг')


class ServiceItem(models.Model):
    tab = models.ForeignKey(ServiceTab, on_delete=models.CASCADE, related_name="items", verbose_name=_("Таб"))
    title = models.CharField(max_length=255, verbose_name=_("Заголовок услуги"))
    description = models.TextField(verbose_name=_("Описание услуги"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Пункт для кнопки')
        verbose_name_plural = _('Пункты для кнопки')


class BannerSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок баннера", blank=True, null=True)
    description = models.TextField(verbose_name="Описание баннера", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Раздел баннер')
        verbose_name_plural = _('Раздел баннера')


class WhyChooseUsSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок секции")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Раздел 'Почему стоит выбрать нас?'")
        verbose_name_plural = _("Раздел 'Почему стоит выбрать нас?'")


class Advantage(models.Model):
    section = models.ForeignKey(WhyChooseUsSection, on_delete=models.CASCADE, related_name="advantages", verbose_name="Секция")
    title = models.CharField(max_length=255, verbose_name="Заголовок преимущества")
    description = models.TextField(verbose_name="Описание преимущества")
    image = models.FileField(upload_to="advantage_images/", verbose_name="Изображение преимущества")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Преимущество")
        verbose_name_plural = _("Преимуществa")


class StatisticsSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Статистика")
        verbose_name_plural = _("Статистика")

    def __str__(self):
        return self.title


class StatisticItem(models.Model):
    section = models.ForeignKey(StatisticsSection, on_delete=models.CASCADE, related_name="statistics", verbose_name=_("Секция"))
    title = models.CharField(max_length=255, verbose_name=_("Название статистики"))
    value = models.IntegerField(verbose_name=_("Значение"))
    icon = models.FileField(upload_to="statistics_icons/", verbose_name=_("Иконка"))

    class Meta:
        verbose_name = _("Статистика")
        verbose_name_plural = _("Статистика")

    def __str__(self):
        return f"{self.title}: {self.value}"


class FAQSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Часто задаваемые вопросы")
        verbose_name_plural = _("Часто задаваемые вопросы")

    def __str__(self):
        return self.title


class FAQItem(models.Model):
    section = models.ForeignKey(FAQSection, on_delete=models.CASCADE, related_name="faq_items", verbose_name=_("Секция"))
    question = models.CharField(max_length=255, verbose_name=_("Вопрос"))
    answer = models.TextField(verbose_name=_("Ответ"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    def __str__(self):
        return self.question


class HappyCustomersSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Раздел 'Наши счастливые клиенты'")
        verbose_name_plural = _("Раздел 'Наши счастливые клиенты'")

    def __str__(self):
        return self.title


class HappyCustomer(models.Model):
    section = models.ForeignKey(HappyCustomersSection, on_delete=models.CASCADE, related_name="customers", verbose_name=_("Секция"))
    image = models.ImageField(upload_to="customer_images/", blank=True, null=True, verbose_name=_("Изображение"))
    video = models.FileField(upload_to="customer_videos/", blank=True, null=True, verbose_name=_("Видео"))

    class Meta:
        verbose_name = _("Счастливый клиент")
        verbose_name_plural = _("Счастливые клиенты")

    def __str__(self):
        return f"Клиент #{self.pk}"


class BlogSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Раздел 'Блог'")
        verbose_name_plural = _("Раздел 'Блог'")

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    section = models.ForeignKey(BlogSection, on_delete=models.CASCADE, related_name="posts", verbose_name=_("Секция"))
    content = models.TextField(verbose_name=_("Текст поста"))
    video = models.FileField(upload_to="blog_videos/", blank=True, null=True, verbose_name=_("Видео"))

    class Meta:
        verbose_name = _("Блог пост")
        verbose_name_plural = _("Блог посты")

    def __str__(self):
        return f"Пост #{self.pk}"


class FooterSection(SingletonModel):
    about_text = models.TextField(verbose_name=_("Текст о компании"))
    title_address = models.CharField(verbose_name=_("Заголовок 'Адрес'"), blank=True, null=True)
    title_work_time = models.CharField(verbose_name=_("Заголовок 'Время работы'"), blank=True, null=True)
    logo = models.FileField(upload_to="footer/", verbose_name=_("Логотип"))

    class Meta:
        verbose_name = _("Раздел Футер")
        verbose_name_plural = _("Раздел Футеры")

    def __str__(self):
        return "Футер"


class LocationInfoFooter(SingletonModel):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="address", verbose_name=_("Секция"))
    logo = models.FileField(upload_to="footer/", verbose_name=_("Логотип"), blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name=_("Адресс"), blank=True, null=True)
    link = models.URLField(verbose_name=_("Ссылка на Адрес"), blank=True, null=True)
    map_iframe = models.TextField(verbose_name=_("Iframe код для карты"), blank=True, null=True)


class PhoneInfoFooter(SingletonModel):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="phone", verbose_name=_("Секция"))
    logo = models.FileField(upload_to="footer/", verbose_name=_("Логотип"), blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name=_("Телефон"), blank=True, null=True)
    link = models.URLField(verbose_name=_("Ссылка на Whats App"), blank=True, null=True)


class EmailInfoFooter(SingletonModel):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="email", verbose_name=_("Секция"))
    logo = models.FileField(upload_to="footer/", verbose_name=_("Логотип"), blank=True, null=True)
    email = models.CharField(max_length=255, verbose_name=_("Email"), blank=True, null=True)
    link = models.URLField(verbose_name=_("Ссылка на Email"), blank=True, null=True)


class WorkHour(models.Model):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="work_hours", verbose_name=_("Секция"))
    day = models.CharField(max_length=20, verbose_name=_("День"))
    open_time = models.CharField(max_length=20, verbose_name=_("Время открытия"))
    close_time = models.CharField(max_length=20, verbose_name=_("Время закрытия"))
    is_closed = models.BooleanField(default=False, verbose_name=_("Выходной"))

    class Meta:
        verbose_name = _("Рабочее время")
        verbose_name_plural = _("Рабочее время")

    def __str__(self):
        if self.is_closed:
            return f"{self.day}: Выходной"
        return f"{self.day}: {self.open_time} - {self.close_time}"


class PaymentMethod(models.Model):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="payment_methods", verbose_name=_("Секция"))
    icon = models.FileField(upload_to="footer/payment/", verbose_name=_("Иконка метода оплаты"))

    class Meta:
        verbose_name = _("Метод оплаты")
        verbose_name_plural = _("Методы оплаты")

    def __str__(self):
        return f"Метод оплаты"


class SocialMedia(models.Model):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name="socials", verbose_name=_("Секция"))
    name = models.CharField(max_length=50, verbose_name=_("Название соц. сети"))
    url = models.URLField(verbose_name=_("Ссылка на соц. сеть"))
    icon = models.FileField(upload_to="footer/socials/", verbose_name=_("Иконка соц. сети"))

    class Meta:
        verbose_name = _("Социальная сеть")
        verbose_name_plural = _("Социальные сети")

    def __str__(self):
        return f"Соц. сеть: {self.name}"


class AboutSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Раздел 'О нас'")
        verbose_name_plural = _("Раздел 'О нас'")

    def __str__(self):
        return self.title


class AboutBlock(models.Model):
    section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name="blocks", verbose_name=_("Секция"))
    image = models.ImageField(upload_to="about_images/", verbose_name=_("Изображение"))
    text = models.TextField(verbose_name=_("Описание"))
    is_reversed = models.BooleanField(default=False, verbose_name=_("Отображение текста слева"))

    class Meta:
        verbose_name = _("О нас: Блок")
        verbose_name_plural = _("О нас: Блоки")

    def __str__(self):
        return f"Блок в секции '{self.section.title}'"


class TeamSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Раздел 'Наша команда'")
        verbose_name_plural = _("Раздел 'Наша команда'")

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    section = models.ForeignKey(TeamSection, on_delete=models.CASCADE, related_name="members", verbose_name=_("Секция"))
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    position = models.CharField(max_length=255, verbose_name=_("Должность"))
    image = models.ImageField(upload_to="team_images/", verbose_name=_("Фотография"))

    class Meta:
        verbose_name = _("Член команды")
        verbose_name_plural = _("Члены команды")

    def __str__(self):
        return self.name


class GoogleSection(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок секции"))

    class Meta:
        verbose_name = _("Раздел 'Google отзыв'")
        verbose_name_plural = _("Раздел 'Google отзывы'")

    def __str__(self):
        return self.title


class GoogleReview(models.Model):
    section = models.ForeignKey(GoogleSection, on_delete=models.CASCADE, related_name="google", verbose_name=_("Секция"))
    reviewer_name = models.CharField(max_length=255, verbose_name=_("Имя пользователя"))
    rating = models.IntegerField(verbose_name=_("Рейтинг"))
    text = models.TextField(verbose_name=_("Текст отзыва"))
    avatar_url = models.URLField(blank=True, null=True, verbose_name=_("URL аватара"))

    class Meta:
        verbose_name = _("Отзыв Google")
        verbose_name_plural = _("Отзывы Google")

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}"


class SiteSettings(SingletonModel):
    meta_title = models.CharField(max_length=255, verbose_name=_("Мета заголовок"), blank=True, null=True)
    meta_description = models.CharField(max_length=255, verbose_name=_("Мета описание"), blank=True, null=True)
    meta_image = models.ImageField(upload_to="images/meta", verbose_name=_("Мета изображение"), blank=True, null=True)

    def str(self):
        return self.site_name

    class Meta:
        verbose_name = _("Настройки сайта")
        verbose_name_plural = _("Настройки сайта")
