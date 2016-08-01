from django.db import models


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
