from django.db import models


class Source(models.Model):
    source_short_description = models.CharField('Краткое описание', max_length=250)
    source_full_description = models.TextField('Полное описание', )

    def __str__(self):
        return self.source_short_description

    class Meta:
        verbose_name = 'Источник'
        verbose_name_plural = 'Источники'


class Appliances(models.Model):
    appliances_type = models.CharField('Тип прибора', max_length=250)
    appliances_model = models.TextField('Модели', )
    appliances_paramerts = models.CharField('Параметры', max_length=300)
    appliances_manufacturer = models.CharField('Производитель', max_length=300)

    def __str__(self):
        return self.appliances_model

    class Meta:
        verbose_name = 'Прибор'
        verbose_name_plural = 'Приборы'


class Measurable(models.Model):
    measurable_parametrs = models.CharField('Название параметра', max_length=300)

    # measurable_value = models.DecimalField('Значение', max_digits=19, decimal_places=10)

    def __str__(self):
        return self.measurable_parametrs

    class Meta:
        verbose_name = 'Название измерямого параметра'
        verbose_name_plural = 'Названия измеряемых параметров'


class Expirement(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.OneToOneField(Source, null=True, on_delete=models.PROTECT, verbose_name='Источник')
    experiment_scheme = models.ImageField(upload_to='images/', verbose_name='Схема эксперимента')
    measurements = models.CharField('Размеры (метры)', max_length=100)
    appliance = models.ForeignKey(Appliances, null=True, on_delete=models.PROTECT, verbose_name='Приборы')
    places = models.CharField('Научный центр', max_length=250)
    measurable = models.ForeignKey(Measurable, null=True, on_delete=models.PROTECT, verbose_name='Измеряемые параметры')
    value = models.DecimalField(verbose_name='Значение', decimal_places=10, max_digits=30)
    configurate_liquid = models.CharField('Конфигурация жидкости', null=True, max_length=200)
    effects = models.CharField('Эффект', max_length=300)

    class Meta:
        verbose_name = 'Эксперимент'
        verbose_name_plural = 'Эксперименты'
