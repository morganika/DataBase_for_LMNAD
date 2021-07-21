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
    measurable_parametrs = models.CharField('Параметр', null=True, max_length=250)
    measurable_value = models.CharField('Значение', null=True, max_length=250)

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
    appliance = models.ManyToManyField(Appliances, verbose_name='Приборы')
    places = models.CharField('Научный центр', max_length=250)
    measurable = models.ManyToManyField(Measurable, verbose_name='Измеряемые параметры')
    configurate_liquid = models.CharField('Конфигурация жидкости', null=True, max_length=200)
    effects = models.CharField('Эффект', max_length=300)
    measured_param = models.CharField('Измеряемые параметры', max_length=300, null=True)

    def __str__(self):
        return self.effects

    class Meta:
        verbose_name = 'Эксперимент'
        verbose_name_plural = 'Эксперименты'
