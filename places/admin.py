from django.contrib import admin
from django.utils.html import format_html
from .models import Place, PlaceImage
from adminsortable2.admin import SortableInlineAdminMixin

import traceback

class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width = 'auto',
            height = '200',
            )
    )

    fields = ('image', 'image_preview')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    try:
        inlines = [
            PlaceImageInline,
        ]
    except Exception:
        print(traceback.format_exc())

    search_fields = ['title']

admin.site.register(PlaceImage)