from django.contrib import admin

from .models import Source, Appliances, Measurable


class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_short_description', 'source_full_description')
    list_display_links = ('source_short_description',)
    search_fields = ('source_short_description',)


class AppliancesAdmin(admin.ModelAdmin):
    list_display = ('appliances_type', 'appliances_model')
    list_display_links = ('appliances_model')


class MeasurableAdmin(admin.ModelAdmin):
    list_display = ('measurable_parametrs',)
    list_display_links = ('measurable_parametrs',)


admin.site.register(Source, SourceAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Measurable, MeasurableAdmin)