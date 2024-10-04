import nested_admin

from django.contrib import admin, messages

from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from apps.service.reviews import fetch_google_reviews
from .models import (
    ContactInfo,
    NavigationLink,
    HeroSlide,
    AdvantageIconText,
    FeaturesSection,
    FeatureItem,
    ServicesSection,
    ServiceTab,
    ServiceItem,
    BannerSection,
    WhyChooseUsSection,
    Advantage,
    StatisticsSection,
    StatisticItem,
    FAQSection,
    FAQItem,
    HappyCustomersSection,
    HappyCustomer,
    BlogSection,
    BlogPost,
    FooterSection,
    LocationInfoFooter,
    PhoneInfoFooter,
    EmailInfoFooter,
    WorkHour,
    PaymentMethod,
    SocialMedia,
    AboutSection,
    AboutBlock,
    TeamSection,
    TeamMember,
    GoogleReview, GoogleSection,
    SiteSettings
)



@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin, TabbedTranslationAdmin, TranslationAdmin):
    list_display = ('title', 'phone_number', 'phone_link')

    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return True


@admin.register(NavigationLink)
class NavigationLinkAdmin(ModelAdmin, TabbedTranslationAdmin, TranslationAdmin):
    list_display = ('home', 'services', 'about_us', 'contacts')

    def has_add_permission(self, request):
        # Prevent more than one instance
        if NavigationLink.objects.exists():
            return False
        return True


class AdvantageIconTextInline(TabularInline, TranslationTabularInline):
    model = AdvantageIconText
    extra = 0


@admin.register(HeroSlide)
class HeroSlideAdmin(ModelAdmin, TabbedTranslationAdmin, TranslationAdmin):
    inlines = [AdvantageIconTextInline]
    list_display = ('title', 'whatsapp_text', 'call_text', 'best_in_town_text', 'rating_text')


class FeatureItemInline(TabularInline, TranslationTabularInline):
    model = FeatureItem
    extra = 0


@admin.register(FeaturesSection)
class FeaturesSectionAdmin(ModelAdmin, TabbedTranslationAdmin, TranslationAdmin):
    inlines = [FeatureItemInline]
    list_display = ('title',)

    def has_add_permission(self, request):
        if FeaturesSection.objects.exists():
            return False
        return True


class ServiceItemInline(nested_admin.NestedTabularInline, TabularInline):  # Use only NestedTabularInline
    model = ServiceItem
    extra = 0
    exclude = ('title', 'description')


class ServiceTabInline(nested_admin.NestedTabularInline, TabularInline):  # Use only NestedTabularInline
    model = ServiceTab
    inlines = [ServiceItemInline]
    extra = 0
    exclude = ('title',)


# Admin for ServicesSection
@admin.register(ServicesSection)
class ServicesSectionAdmin(nested_admin.NestedModelAdmin, ModelAdmin, TabbedTranslationAdmin):  # Use NestedModelAdmin and TabbedTranslationAdmin
    inlines = [ServiceTabInline]

    def has_add_permission(self, request):
        if ServicesSection.objects.exists():
            return False
        return True


@admin.register(BannerSection)
class BannerSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        if BannerSection.objects.exists():
            return False
        return True


class AdvantageInline(TabularInline, TranslationTabularInline):
    model = Advantage
    extra = 0


@admin.register(WhyChooseUsSection)
class WhyChooseUsSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)
    inlines = [AdvantageInline]

    def has_add_permission(self, request):
        if WhyChooseUsSection.objects.exists():
            return False
        return True


class StatisticItemInline(TabularInline, TranslationTabularInline):
    model = StatisticItem
    extra = 0


@admin.register(StatisticsSection)
class StatisticsSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)
    inlines = [StatisticItemInline]

    def has_add_permission(self, request):
        if StatisticsSection.objects.exists():
            return False
        return True


class FAQItemInline(TabularInline, TranslationTabularInline):
    model = FAQItem
    extra = 0


@admin.register(FAQSection)
class FAQSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        if FAQSection.objects.exists():
            return False
        return True

    inlines = [FAQItemInline]


class HappyCustomerInline(TabularInline):
    model = HappyCustomer
    extra = 0


@admin.register(HappyCustomersSection)
class HappyCustomersSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        if HappyCustomersSection.objects.exists():
            return False
        return True

    inlines = [HappyCustomerInline]


class BlogPostInline(TabularInline, TranslationTabularInline):
    model = BlogPost
    extra = 0


@admin.register(BlogSection)
class BlogSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        if BlogSection.objects.exists():
            return False
        return True

    inlines = [BlogPostInline]


class LocationInfoFooterInline(TabularInline, TranslationTabularInline):
    model = LocationInfoFooter
    extra = 0

    def has_add_permission(self, request, obj=None):
        if LocationInfoFooter.objects.count() >= 1:
            return False
        return True


class PhoneInfoFooterInline(TabularInline):
    model = PhoneInfoFooter
    extra = 0

    def has_add_permission(self, request, obj=None):
        if PhoneInfoFooter.objects.count() >= 1:
            return False
        return True


class EmailInfoFooterInline(TabularInline):
    model = EmailInfoFooter
    extra = 0

    def has_add_permission(self, request, obj=None):
        if EmailInfoFooter.objects.count() >= 1:
            return False
        return True


class WorkHourInline(TabularInline):
    model = WorkHour
    extra = 0


class PaymentMethodInline(TabularInline):
    model = PaymentMethod
    extra = 0


class SocialMediaInline(TabularInline):
    model = SocialMedia
    extra = 0


@admin.register(FooterSection)
class FooterSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('about_text',)

    def has_add_permission(self, request):
        if FooterSection.objects.exists():
            return False
        return True

    inlines = [LocationInfoFooterInline, PhoneInfoFooterInline, EmailInfoFooterInline,
               WorkHourInline, PaymentMethodInline, SocialMediaInline]


class AboutBlockInline(TabularInline, TranslationTabularInline):
    model = AboutBlock
    extra = 0


@admin.register(AboutSection)
class AboutSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        if AboutSection.objects.exists():
            return False
        return True

    inlines = [AboutBlockInline]


# class TeamMemberInline(TabularInline, TranslationTabularInline):
#     model = TeamMember
#     extra = 0
#
#
# @admin.register(TeamSection)
# class TeamSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
#     list_display = ('title',)
#
#     def has_add_permission(self, request):
#         if TeamSection.objects.exists():
#             return False
#         return True
#
#     inlines = [TeamMemberInline]


class GoogleReviewInline(TabularInline):
    model = GoogleReview
    extra = 0


@admin.register(GoogleSection)
class GoogleSectionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)
    inlines = [GoogleReviewInline]
    actions = ['load_google_reviews']

    def has_add_permission(self, request):
        if GoogleSection.objects.exists():
            return False
        return True

    def load_google_reviews(self, request, queryset):
        try:
            # Удаляем все существующие отзывы перед загрузкой
            GoogleReview.objects.all().delete()

            # Загружаем новые отзывы
            fetch_google_reviews()  # Вызов функции загрузки отзывов

            self.message_user(request, "Отзывы успешно загружены.", messages.SUCCESS)
        except Exception as e:
            self.message_user(request, f"Ошибка при загрузке отзывов: {e}", messages.ERROR)

    load_google_reviews.short_description = "Загрузить отзывы с Google"


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('meta_title',)

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True
