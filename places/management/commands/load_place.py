import requests
from places.models import Place, PlaceImage
from django.core.management.base import BaseCommand
from django.core import files
from io import BytesIO


class Command(BaseCommand):
    help = 'Add new places'

    def add_arguments(self, parser):
        parser.add_argument('url')

    def handle(self, *args, **options):

        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in decoded_response:
            raise requests.exceptions.HTTPError(decoded_response['error'])
        place, create = Place.objects.get_or_create(
            title=decoded_response['title'],
            defaults={
                "short_description": decoded_response['description_short'],
                "long_description": decoded_response['description_long'],
                "lng": decoded_response['coordinates']['lng'],
                "lat": decoded_response['coordinates']['lat']})
        image_urls = decoded_response['imgs']

        for number, image_url in enumerate(image_urls, 1):
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = image_url.split('/')[-1]
            placeimage, create = PlaceImage.objects.get_or_create(
                place=place,
                number=number)
            byte_response = BytesIO(response.content)
            placeimage.image.save(
                image_name,
                files.File(byte_response),
                save=True)
