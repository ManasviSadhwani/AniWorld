from django.contrib import admin
from .models import Ngo
from django.utils.html import format_html

# Register your models here.

class NgoAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'name', 'myphoto', 'established')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'city')
    list_filter = ('awards', 'city')



admin.site.register(Ngo, NgoAdmin)
