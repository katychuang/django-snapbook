from django.contrib import admin

from example.models import *

class StyleAdmin(admin.ModelAdmin):
    list_display_links = ('font',)
    list_display = ('font','section')
    save_as         = True

admin.site.register(Style, StyleAdmin)
