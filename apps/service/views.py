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
    footer = FooterSection.objects.annotate(
        day_order=Case(
            When(work_hours__day="Понедельник", then=Value(1)),
            When(work_hours__day="Вторник", then=Value(2)),
            When(work_hours__day="Среда", then=Value(3)),
            When(work_hours__day="Четверг", then=Value(4)),
            When(work_hours__day="Пятница", then=Value(5)),
            When(work_hours__day="Суббота", then=Value(6)),
            When(work_hours__day="Воскресенье", then=Value(7)),
            output_field=IntegerField(),
        )
    ).order_by('day_order').first()
    google_section = GoogleSection.objects.first()
    site_meta = SiteSettings.objects.first()
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
    footer = FooterSection.objects.first()
    about_section = AboutSection.objects.first()
    team_section = TeamSection.objects.first()
    google_section = GoogleSection.objects.first()
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
    footer = FooterSection.objects.first()
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
    footer = FooterSection.objects.first()
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
    })
