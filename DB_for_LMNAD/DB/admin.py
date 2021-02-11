from django.contrib import admin

from .models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_short_description', 'source_full_description')
    list_display_links = ('source_short_description',)
    search_fields = ('source_short_description',)


admin.site.register(Source, SourceAdmin)
