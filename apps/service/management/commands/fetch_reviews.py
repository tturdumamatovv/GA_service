from django.core.management.base import BaseCommand
from apps.service.reviews import fetch_google_reviews


class Command(BaseCommand):
    help = "Fetch and save Google reviews."

    def handle(self, *args, **kwargs):
        fetch_google_reviews()
        self.stdout.write(self.style.SUCCESS('Successfully fetched Google reviews'))
