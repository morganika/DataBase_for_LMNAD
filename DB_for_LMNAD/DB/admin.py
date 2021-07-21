from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Source, Appliances, Measurable, Expirement

from itertools import chain


class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_short_description', 'source_full_description')
    list_display_links = ('source_short_description',)
    search_fields = ('source_short_description',)


class AppliancesAdmin(admin.ModelAdmin):
    list_display = ('appliances_type', 'appliances_model', 'appliances_paramerts', 'appliances_manufacturer')
    list_display_links = ('appliances_model',)
    search_fields = ('appliances_model',)


class MeasurableAdmin(admin.ModelAdmin):
    list_display = ('measurable_parametrs', 'measurable_value')
    list_display_links = ('measurable_parametrs',)
    list_filter = ('measurable_parametrs',)
    search_fields = ('measurable_value',)


class ExpirementAdmin(admin.ModelAdmin):
    def applience_names(self, obj):
        a = obj.appliance.values_list('appliances_model')
        return list(chain.from_iterable(a))
    applience_names.short_description = 'Приборы'

    def get_image(self, obj):
        return mark_safe(
            f'<a href={obj.experiment_scheme.url}><img src={obj.experiment_scheme.url} widht="100" height="100"</a>')

    get_image.short_description = "Изображение"

    readonly_fields = ("get_image",)

    def measurable_names(self, obj):
        a = obj.measurable.values_list('measurable_parametrs', 'measurable_value')
        return list(chain.from_iterable(a))
    measurable_names.short_description = 'Начальные параметры'

    list_display = ('source', 'get_image', 'effects', 'applience_names', 'measurements', 'places', 'measured_param', 'measurable_names', 'configurate_liquid')
    list_display_links = ('source',)
    list_filter = ('configurate_liquid', 'effects', 'measurable__measurable_parametrs',)
    search_fields = ('configurate_liquid', 'effects', 'appliance__appliances_model', 'measurable__measurable_value','measured_param')


admin.site.register(Source, SourceAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Measurable, MeasurableAdmin)
admin.site.register(Expirement, ExpirementAdmin)
