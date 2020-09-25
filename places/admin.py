from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage
from adminsortable2.admin import SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" height={height} />',
            url=obj.image.url,
            height='200',
            )

    fields = ['image', 'image_preview']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    inlines = [
        PlaceImageInline,
    ]

    search_fields = ['title']


admin.site.register(PlaceImage)
