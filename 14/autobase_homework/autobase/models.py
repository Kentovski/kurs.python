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
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)


class Auto(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    body = models.CharField(choices=AUTO_BODY, max_length=12)
    fuelType = models.CharField(max_length=8, choices=(
            ('petrol', 'Petrol'),
            ('diesel', 'Diesel'),
            ('gas', 'Gas'),
            ('electric', 'Electric'),
        )
    )
    fuelRate = models.FloatField()
    engineVolume = models.FloatField()
    enginePower = models.FloatField()
    gearbox = models.CharField(max_length=9, choices=(
            ('manual', 'Manual'),
            ('auto', 'Automatic'),
            ('tiptronic', 'Tiptronic'),
            ('adaptive', 'Adaptive'),
            ('vary', 'Variable'),
        )
    )
    year = models.DateField()
