from django.contrib import admin
from . models import Vets
from django.utils.html import format_html

# Register your models here.

class VetsAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'clinic', 'fee')
    list_display_links = ('id', 'name')
    search_fields = ('city', 'name')
    list_filter = ('name', 'city')

admin.site.register(Vets, VetsAdmin)
