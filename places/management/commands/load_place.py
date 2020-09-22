import os
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
        place_json = response.json()
        place, create = Place.objects.get_or_create(title=place_json['title'],
                                    description_short=place_json['description_short'],
                                    description_long=place_json['description_long'],
                                    lng=place_json['coordinates']['lng'],
                                    lat=place_json['coordinates']['lat']
                                    )
        image_urls = place_json['imgs']
                                                             
        for number, image_url in enumerate(image_urls, 1):
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = image_url.split('/')[-1]
            BASE_DIR = os.getcwd().split('/')[-1]
            image_with_path = os.path.join(BASE_DIR, 'media', 'media', image_name)
            placeimage, create = PlaceImage.objects.get_or_create(place=place, number=number)
            img_byte = BytesIO(response.content)
            placeimage.image.save(image_with_path, files.File(img_byte), save=True)
