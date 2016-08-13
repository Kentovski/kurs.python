from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


AUTO_BODY = (
    ('Passenger', (
            ('sedan', _('Седан')),
            ('hatchback', _('Хэтчбэк')),
            ('limo', _('Лимузин')),
            ('crossover', _('Кроссовер')),
            ('universal', _('Универсал')),
            ('cabriole', _('Кабриолет')),
            ('minivan', _('Минивэн')),
            ('pickup', _('Пикап')),
            ('offroad', _('Внедорожник')),
        )
    ),
    ('Lorry', (
            ('trans', _('Транспортировщик')),
            ('tow', _('Тягач')),
            ('log', _('Лесовоз')),
            ('dump', _('Самосвал')),
            ('refrigerator', _('Холодильник')),
        )
    ),
    ('Autobus', (
            ('mini', _('Мини-автобус')),
            ('city', _('Городской')),
            ('double', _('Двухэтажный')),
        )
    ),
)


class Manufacturer(models.Model):
    brand = models.CharField(max_length=50, unique=True, default='Noname')
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = _("Производитель")
        verbose_name_plural = _("Производители")


class Auto(models.Model):
    name =  models.CharField(max_length=50, default='Noname')
    manufacturer = models.ForeignKey(Manufacturer)
    body = models.CharField(choices=AUTO_BODY, max_length=12)
    fuelType = models.CharField(max_length=8, choices=(
            ('petrol', _('Бензин')),
            ('diesel', _('Дизель')),
            ('gas', _('Газ')),
            ('electric', _('Электричество')),
            ('hibrid', _('Гибрид')),
        )
    )
    fuelRate = models.FloatField()
    engineVolume = models.FloatField()
    enginePower = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=9, choices=(
            ('manual', _('Ручная')),
            ('auto', _('Автоматическая')),
            ('tiptronic', _('Типтоник')),
            ('adaptive', _('Адаптивная')),
            ('vary', _('Вариативная')),
        )
    )
    year = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.manufacturer.brand, self.name)

    class Meta:
        verbose_name = _("Автомобиль")
        verbose_name_plural = _("Автомобили")


class Warehouse(models.Model):
    product = models.OneToOneField(Auto)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _("Склад")
        verbose_name_plural = _("Склад")


class Buyer(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[
            RegexValidator(
                regex='0\d{2,3}\s?[0-9\-]+',
                message=_('Номер должен быть в формате 0хх 1234567 или 0хх 123-45-67')
            )
        ]
    )

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)

    class Meta:
        verbose_name = _("Покупатель")
        verbose_name_plural = _("Покупатели")


class Orders(models.Model):
    goods = models.ForeignKey(Auto)
    amount = models.PositiveSmallIntegerField()
    buyer = models.ForeignKey(Buyer)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}шт.'.format(self.goods.name, self.amount)

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
