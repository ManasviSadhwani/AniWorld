from django.contrib import admin
from . models import Adoption
from django.utils.html import format_html

# Register your models here.

class AdAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'animal', 'myphoto', 'breed')
    list_display_links = ('id', 'animal')
    search_fields = ('animal', 'breed')
    list_filter = ('animal', 'city')

admin.site.register(Adoption, AdAdmin)