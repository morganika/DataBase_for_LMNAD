from django.db import models


class Source(models.Model):
    source_short_description = models.CharField('Краткое описание', max_length=250)
    source_full_description = models.TextField('Полное описание', )

    def __str__(self):
        return self.source_short_description

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'
