from modeltranslation.translator import register, TranslationOptions
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
    BlogSection,
    BlogPost,
    FooterSection,
    LocationInfoFooter,
    WorkHour,
    AboutBlock,
    AboutSection,
    TeamSection,
    TeamMember,
    GoogleSection, GoogleReview
)


@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'opening_time_title', 'opening_days')  # Fields to translate


@register(NavigationLink)
class NavigationLinkTranslationOptions(TranslationOptions):
    fields = ('home', 'services', 'about_us', 'contacts')


@register(HeroSlide)
class HeroSlideTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle1', 'subtitle2', 'whatsapp_text', 'call_text', 'best_in_town_text', 'rating_text')


@register(AdvantageIconText)
class AdvantageIconTextTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(FeaturesSection)
class FeaturesSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FeatureItem)
class FeatureItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServicesSection)
class ServicesSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServiceTab)
class ServiceTabTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServiceItem)
class ServiceItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(BannerSection)
class BannerSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(WhyChooseUsSection)
class WhyChooseUsSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(StatisticsSection)
class StatisticsSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(StatisticItem)
class StatisticItemTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FAQSection)
class FAQSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FAQItem)
class FAQSectionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(HappyCustomersSection)
class HappyCustomersSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogSection)
class BlogSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(FooterSection)
class FooterSectionTranslationOptions(TranslationOptions):
    fields = ('about_text', 'title_address', 'title_work_time')


@register(LocationInfoFooter)
class LocationInfoFooterTranslationOptions(TranslationOptions):
    fields = ('address',)


@register(WorkHour)
class WorkHourTranslationOptions(TranslationOptions):
    fields = ('weekend',)


@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(AboutBlock)
class AboutBlockTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(TeamSection)
class TeamSectionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


@register(GoogleSection)
class GoogleSectionTranslationOptions(TranslationOptions):
    fields = ('title',)
