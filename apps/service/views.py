from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField
from .models import (
    ContactInfo,
    NavigationLink,
    HeroSlide,
    FeaturesSection,
    ServicesSection,
    BannerSection,
    WhyChooseUsSection,
    StatisticsSection,
    FAQSection,
    HappyCustomersSection,
    BlogSection,
    FooterSection,
    AboutSection,
    TeamSection,
    SiteSettings, GoogleSection
)

DAYS_ORDER = {
    "Понедельник": 1,
    "Вторник": 2,
    "Среда": 3,
    "Четверг": 4,
    "Пятница": 5,
    "Суббота": 6,
    "Воскресенье": 7,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}

def index(request):
    contact_info = ContactInfo.objects.all()
    navigation = NavigationLink.objects.first()
    hero_slides = HeroSlide.objects.prefetch_related('advantages').all()
    features_section = FeaturesSection.objects.first()
    services_section = ServicesSection.objects.prefetch_related('tabs__items').first()
    banner_section = BannerSection.objects.first()
    why_choose_us = WhyChooseUsSection.objects.first()
    statistics_section = StatisticsSection.objects.first()
    faq_section = FAQSection.objects.first()
    happy_customers_section = HappyCustomersSection.objects.first()
    blog_section = BlogSection.objects.first()
    footer = FooterSection.objects.prefetch_related('work_hours').first()
    google_section = GoogleSection.objects.first()
    site_meta = SiteSettings.objects.first()
    footer_work_hours = sorted(footer.work_hours.all(), key=lambda x: DAYS_ORDER.get(x.day, 0))
    return render(request, 'index.html', {
        'contact_info': contact_info,
        'navigation': navigation,
        'hero_slides': hero_slides,
        'features_section': features_section,
        'services_section': services_section,
        'banner_section': banner_section,
        'why_choose_us': why_choose_us,
        'statistics_section': statistics_section,
        'faq_section': faq_section,
        'happy_customers_section': happy_customers_section,
        'blog_section': blog_section,
        'footer': footer,
        'footer_work_hours': footer_work_hours,
        'google_section': google_section,
        'site_meta': site_meta,
    })


def about(request):
    contact_info = ContactInfo.objects.all()
    navigation = NavigationLink.objects.first()
    hero_slides = HeroSlide.objects.prefetch_related('advantages').all()
    features_section = FeaturesSection.objects.first()
    services_section = ServicesSection.objects.prefetch_related('tabs__items').first()
    banner_section = BannerSection.objects.first()
    why_choose_us = WhyChooseUsSection.objects.first()
    statistics_section = StatisticsSection.objects.first()
    faq_section = FAQSection.objects.first()
    happy_customers_section = HappyCustomersSection.objects.first()
    blog_section = BlogSection.objects.first()
    footer = FooterSection.objects.prefetch_related('work_hours').first()
    about_section = AboutSection.objects.first()
    team_section = TeamSection.objects.first()
    google_section = GoogleSection.objects.first()
    footer_work_hours = sorted(footer.work_hours.all(), key=lambda x: DAYS_ORDER.get(x.day, 0))
    return render(request, 'about-us.html', {
        'contact_info': contact_info,
        'navigation': navigation,
        'hero_slides': hero_slides,
        'features_section': features_section,
        'services_section': services_section,
        'banner_section': banner_section,
        'why_choose_us': why_choose_us,
        'statistics_section': statistics_section,
        'faq_section': faq_section,
        'happy_customers_section': happy_customers_section,
        'blog_section': blog_section,
        'footer': footer,
        'footer_work_hours': footer_work_hours,
        'about_section': about_section,
        'team_section': team_section,
        'google_section': google_section,
    })


def service(request):
    contact_info = ContactInfo.objects.all()
    navigation = NavigationLink.objects.first()
    hero_slides = HeroSlide.objects.prefetch_related('advantages').all()
    features_section = FeaturesSection.objects.first()
    services_section = ServicesSection.objects.prefetch_related('tabs__items').first()
    banner_section = BannerSection.objects.first()
    why_choose_us = WhyChooseUsSection.objects.first()
    statistics_section = StatisticsSection.objects.first()
    faq_section = FAQSection.objects.first()
    happy_customers_section = HappyCustomersSection.objects.first()
    blog_section = BlogSection.objects.first()
    footer = FooterSection.objects.prefetch_related('work_hours').first()
    footer_work_hours = sorted(footer.work_hours.all(), key=lambda x: DAYS_ORDER.get(x.day, 0))
    return render(request, 'services.html', {
        'contact_info': contact_info,
        'navigation': navigation,
        'hero_slides': hero_slides,
        'features_section': features_section,
        'services_section': services_section,
        'banner_section': banner_section,
        'why_choose_us': why_choose_us,
        'statistics_section': statistics_section,
        'faq_section': faq_section,
        'happy_customers_section': happy_customers_section,
        'blog_section': blog_section,
        'footer': footer,
        'footer_work_hours': footer_work_hours,
    })


def contact(request):
    contact_info = ContactInfo.objects.all()
    navigation = NavigationLink.objects.first()
    hero_slides = HeroSlide.objects.prefetch_related('advantages').all()
    features_section = FeaturesSection.objects.first()
    services_section = ServicesSection.objects.prefetch_related('tabs__items').first()
    banner_section = BannerSection.objects.first()
    why_choose_us = WhyChooseUsSection.objects.first()
    statistics_section = StatisticsSection.objects.first()
    faq_section = FAQSection.objects.first()
    happy_customers_section = HappyCustomersSection.objects.first()
    blog_section = BlogSection.objects.first()
    footer = FooterSection.objects.prefetch_related('work_hours').first()
    footer_work_hours = sorted(footer.work_hours.all(), key=lambda x: DAYS_ORDER.get(x.day, 0))
    return render(request, 'contacts.html', {
        'contact_info': contact_info,
        'navigation': navigation,
        'hero_slides': hero_slides,
        'features_section': features_section,
        'services_section': services_section,
        'banner_section': banner_section,
        'why_choose_us': why_choose_us,
        'statistics_section': statistics_section,
        'faq_section': faq_section,
        'happy_customers_section': happy_customers_section,
        'blog_section': blog_section,
        'footer': footer,
        'footer_work_hours': footer_work_hours,
    })
