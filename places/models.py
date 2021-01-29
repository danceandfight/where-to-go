from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name="Название", max_length=200)
    short_description = models.TextField(
        verbose_name="Короткое описание",
        blank=True,
        )
    long_description = HTMLField(
        verbose_name="Полное описание",
        blank=True,
        )
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фотография', upload_to='media')
    number = models.PositiveIntegerField(
        verbose_name='Номер',
        default=0,
        db_index=True,
        blank=True,
        )

    class Meta(object):
        ordering = ['number']

    def __str__(self):
        return f'{self.number} {self.place.title}'
