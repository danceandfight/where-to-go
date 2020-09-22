from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place, PlaceImage

def serialize_place(place):
    
    return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('show_place_page', args=(place.id,))
          }
        }

def show_main_page(request):
    
    places = Place.objects.all()
    places_content = [serialize_place(place) for place in places]
    places_geojson = {
        'type': 'FeatureCollection',
        'features': places_content,
    }
    return render(request, 'index.html', {'places_geojson': places_geojson})
   
def show_place_page(request, id):
    
    place = get_object_or_404(Place, id=id)
    images = place.place_images.all()
    place_json = {
        "title": place.title,
        "imgs": [image.image.url for image in images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lng,
            "lng": place.lat
        }
    }
    return JsonResponse(place_json, 
                        json_dumps_params={'indent': 2, 'ensure_ascii':False}, 
                        safe=False)