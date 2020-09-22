from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = HTMLField(verbose_name="Полное описание",
                                        blank=True, null=True)
    lng = models.FloatField(verbose_name="Долгота",
                            blank=True, null=True)
    lat = models.FloatField(verbose_name="Широта",
                            blank=True, null=True)
    
    def __str__(self):
        return self.title

class PlaceImage(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место', related_name='place_images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', blank=True, null=True)
    number = models.PositiveIntegerField(verbose_name='Номер', default=0, blank=True, null=True)
    
    
    class Meta(object):
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place.title}'