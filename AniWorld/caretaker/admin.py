from django.contrib import admin
from . models import Caretaker
from django.utils.html import format_html

# Register your models here.

class CtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'price', 'city', 'preferred_animal')
    list_display_links = ('id', 'name')
    search_fields = ('preferred_animal', 'city')
    list_filter = ('preferred_animal', 'city')

admin.site.register(Caretaker, CtAdmin)