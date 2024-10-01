from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Admin GA Service",
    "SITE_HEADER": "Admin GA Service",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    # "SITE_FAVICONS": [
    #     {
    #         "rel": "icon",
    #         "sizes": "32x32",
    #         "type": "image/svg+xml",
    #         "href": lambda request: static("favicon.svg"),
    #     },
    # ],
    "SHOW_HISTORY": False, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
    },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "255 244 230",
            "100": "255 230 204",
            "200": "255 215 179",
            "300": "255 196 143",
            "400": "255 171 87",
            "500": "255 145 0",
            "600": "234 128 0",
            "700": "202 111 0",
            "800": "171 92 0",
            "900": "140 74 0",
            "950": "112 59 0"
        }
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "ru": "🇷🇺",
                "en": "🇬🇧",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Отключить поиск в именах приложений и моделей
        "show_all_applications": True,  # Отключить раскрывающееся меню со всеми приложениями и моделями
        "navigation": [
            {
                "title": _("Заполнение Сайта"),
                "icon": "home",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Контактные информации"),
                        "icon": "call",
                        "link": reverse_lazy("admin:service_contactinfo_changelist"),
                    },
                    {
                        "title": _("Навигационные ссылки"),
                        "icon": "navigation",
                        "link": reverse_lazy("admin:service_navigationlink_changelist"),
                    },
                    {
                        "title": _("Слайды на главной странице"),
                        "icon": "list",
                        "link": reverse_lazy("admin:service_heroslide_changelist"),
                    },
                    {
                        "title": _("Раздел техники"),
                        "icon": "laptop",
                        "link": reverse_lazy("admin:service_featuressection_changelist"),
                    },
                    {
                        "title": _("Раздел услуги"),
                        "icon": "info",
                        "link": reverse_lazy("admin:service_servicessection_changelist"),
                    },
                    {
                        "title": _("Раздел Баннер"),
                        "icon": "ad",
                        "link": reverse_lazy("admin:service_bannersection_changelist"),
                    },
                    {
                        "title": _("Раздел 'Почему стоит выбрать нас?'"),
                        "icon": "star",
                        "link": reverse_lazy("admin:service_whychooseussection_changelist"),
                    },
                    {
                        "title": _("Статистика"),
                        "icon": "equalizer",
                        "link": reverse_lazy("admin:service_statisticssection_changelist"),
                    },
                    {
                        "title": _("Часто задаваемые вопросы"),
                        "icon": "quiz",
                        "link": reverse_lazy("admin:service_faqsection_changelist"),
                    },
                    {
                        "title": _("Раздел 'Наши счастливые клиенты'"),
                        "icon": "mood",
                        "link": reverse_lazy("admin:service_happycustomerssection_changelist"),
                    },
                    {
                        "title": _("Раздел 'Блог'"),
                        "icon": "variables",
                        "link": reverse_lazy("admin:service_blogsection_changelist"),
                    },
                    {
                        "title": _("Раздел Футеры"),
                        "icon": "box",
                        "link": reverse_lazy("admin:service_blogsection_changelist"),
                    },
                    {
                        "title": _("Раздел 'О нас'"),
                        "icon": "publish",
                        "link": reverse_lazy("admin:service_aboutsection_changelist"),
                    },
                    {
                        "title": _("Раздел 'Наша Команда'"),
                        "icon": "group",
                        "link": reverse_lazy("admin:service_teamsection_changelist"),
                    },
                    {
                        "title": _("Раздел 'Google Отзывы'"),
                        "icon": "reviews",
                        "link": reverse_lazy("admin:service_googlesection_changelist"),
                    },

                ],
            },
            {
                "title": _("Мета данные"),
                "icon": "settings",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Мета данные"),
                        "icon": "database",
                        "link": reverse_lazy("admin:service_sitesettings_changelist"),
                    },
                    # {
                    #     "title": _("Заказы"),
                    #     "icon": "archive",
                    #     "link": reverse_lazy("admin:orders_order_changelist"),
                    # },
                    # {
                    #     "title": _("Доставки"),
                    #     "icon": "local_shipping",
                    #     "link": reverse_lazy("admin:orders_delivery_changelist"),
                    # },
                ],
            },
            {
                "title": _("Продукты"),
                "icon": "fastfood",
                "collapsible": True,
                "items": [
                    # {
                    #     "title": _("Продукты"),
                    #     "icon": "local_pizza",
                    #     "link": reverse_lazy("admin:product_product_changelist"),
                    # },
                    # {
                    #     "title": _("Топпинги"),
                    #     "icon": "emoji_food_beverage",
                    #     "link": reverse_lazy("admin:product_topping_changelist"),
                    # },
                    # {
                    #     "title": _("Категории"),
                    #     "icon": "category",
                    #     "link": reverse_lazy("admin:product_category_changelist"),
                    # },
                    # {
                    #     "title": _("Размеры"),
                    #     "icon": "straighten",
                    #     "link": reverse_lazy("admin:product_size_changelist"),
                    # },
                    # {
                    #     "title": _("Теги"),
                    #     "icon": "tag",
                    #     "link": reverse_lazy("admin:product_tag_changelist"),
                    # },
                ],
            },
            {
                "title": _("Страницы"),
                "icon": "description",
                "collapsible": True,
                "items": [
                    # {
                    #     "title": _("Главная страница"),
                    #     "icon": "insert_drive_file",
                    #     "link": reverse_lazy("admin:pages_mainpage_changelist"),
                    # },
                    # {
                    #     "title": _("Статические страницы"),
                    #     "icon": "note_alt",
                    #     "link": reverse_lazy("admin:pages_staticpage_changelist"),
                    # },
                    # {
                    #     "title": _("Баннеры"),
                    #     "icon": "view_carousel",
                    #     "link": reverse_lazy("admin:pages_banner_changelist"),
                    # },
                    # {
                    #     "title": _("Истории"),
                    #     "link": reverse_lazy("admin:pages_stories_changelist"),
                    # },
                    # {
                    #     "title": _("Контакты"),
                    #     "icon": "contact_phone",
                    #     "link": reverse_lazy("admin:pages_contacts_changelist"),
                    # },
                ],
            },
            {
                "title": _("Настройки"),
                "icon": "settings",
                "collapsible": True,
                "items": [
                    # {
                    #     "title": _("Telegram"),
                    #     "icon": "settings",
                    #     "link": reverse_lazy("admin:orders_telegrambottoken_changelist"),
                    # },
                    # {
                    #     "title": _("WhatsApp"),
                    #     "icon": "settings",
                    #     "link": reverse_lazy("admin:orders_whatsappchat_changelist"),
                    # },
                    # {
                    #     "title": _("Кэшбэк"),
                    #     "icon": "settings",
                    #     "link": reverse_lazy("admin:orders_percentcashback_changelist"),
                    # },
                    # {
                    #     "title": _("Тарифы за расстояние"),
                    #     "icon": "settings",
                    #     "link": reverse_lazy("admin:orders_distancepricing_changelist"),
                    # },
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:app_label_model_name_changelist"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}
