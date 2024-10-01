import requests

from decouple import config

from .models import GoogleSection, GoogleReview


def fetch_google_reviews():
    api_key = config('API_KEY')
    place_id = config('PLACE_ID')
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=reviews&key={api_key}"

    response = requests.get(url)
    data = response.json()

    if 'reviews' in data['result']:
        # Получаем или создаем секцию для отзывов Google
        section, created = GoogleSection.objects.get_or_create(title="Отзывы Google")

        for review in data['result']['reviews']:
            GoogleReview.objects.create(
                section=section,
                reviewer_name=review['author_name'],
                rating=review['rating'],
                text=review['text'],
                avatar_url=review.get('profile_photo_url', None),
            )
