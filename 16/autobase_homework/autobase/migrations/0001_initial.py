# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(choices=[('Passenger', (('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('limo', 'Limousine'), ('crossover', 'Crossover'), ('universal', 'Universal'), ('hatchback', 'Hatchback'), ('cabriole', 'Cabriole'), ('minivan', 'Minivan'), ('pickup', 'Pick-up'))), ('Lorry', (('trans', 'Car transporter'), ('tow', 'Tow truck'), ('log', 'Logging truck'), ('dump', 'Dump truck'), ('refrigerator', 'Refrigerator truck'))), ('Autobus', (('mini', 'Minibus'), ('city', 'City bus'), ('double', 'Double-decker')))], max_length=12)),
                ('fuelType', models.CharField(choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('gas', 'Gas'), ('electric', 'Electric')], max_length=8)),
                ('fuelRate', models.FloatField()),
                ('engineVolume', models.FloatField()),
                ('enginePower', models.FloatField()),
                ('gearbox', models.CharField(choices=[('manual', 'Manual'), ('auto', 'Automatic'), ('tiptronic', 'Tiptronic'), ('adaptive', 'Adaptive'), ('vary', 'Variable')], max_length=9)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autobase.Manufacturer'),
        ),
    ]
