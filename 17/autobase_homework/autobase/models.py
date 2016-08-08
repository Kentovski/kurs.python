from django.db import models
from django.core.validators import RegexValidator


AUTO_BODY = (
    ('Passenger', (
            ('sedan', 'Sedan'),
            ('hatchback', 'Hatchback'),
            ('limo', 'Limousine'),
            ('crossover', 'Crossover'),
            ('universal', 'Universal'),
            ('hatchback', 'Hatchback'),
            ('cabriole', 'Cabriole'),
            ('minivan', 'Minivan'),
            ('pickup', 'Pick-up'),
            ('offroad', 'Off-road'),
        )
    ),
    ('Lorry', (
            ('trans', 'Car transporter'),
            ('tow', 'Tow truck'),
            ('log', 'Logging truck'),
            ('dump', 'Dump truck'),
            ('refrigerator', 'Refrigerator truck'),
        )
    ),
    ('Autobus', (
            ('mini', 'Minibus'),
            ('city', 'City bus'),
            ('double', 'Double-decker'),
        )
    ),
)


class Manufacturer(models.Model):
    brand = models.CharField(max_length=50, unique=True, default='Noname')
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Auto(models.Model):
    name =  models.CharField(max_length=50, default='Noname')
    manufacturer = models.ForeignKey(Manufacturer)
    body = models.CharField(choices=AUTO_BODY, max_length=12)
    fuelType = models.CharField(max_length=8, choices=(
            ('petrol', 'Petrol'),
            ('diesel', 'Diesel'),
            ('gas', 'Gas'),
            ('electric', 'Electric'),
            ('hibrid', 'Hibrid'),
        )
    )
    fuelRate = models.FloatField()
    engineVolume = models.FloatField()
    enginePower = models.PositiveIntegerField()
    gearbox = models.CharField(max_length=9, choices=(
            ('manual', 'Manual'),
            ('auto', 'Automatic'),
            ('tiptronic', 'Tiptronic'),
            ('adaptive', 'Adaptive'),
            ('vary', 'Variable'),
        )
    )
    year = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.manufacturer.brand, self.name)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Warehouse(models.Model):
    product = models.OneToOneField(Auto)
    quantity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склад"


class Buyer(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[
            RegexValidator(
                regex='0\d{2,3}\s?[0-9\-]+',
                message='Номер должен быть в формате 0хх 1234567 или 0хх 123-45-67'
            )
        ]
    )

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Orders(models.Model):
    goods = models.ForeignKey(Auto)
    amount = models.PositiveSmallIntegerField()
    buyer = models.ForeignKey(Buyer)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}шт.'.format(self.goods.name, self.amount)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
