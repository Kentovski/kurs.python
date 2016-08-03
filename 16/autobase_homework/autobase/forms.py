from django.forms import ModelForm, TextInput, Select, NumberInput, DateInput
from .models import Manufacturer, Auto


class CreateAuto(ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'manufacturer': Select(attrs={'required': True, 'class': 'form-control'}),
            'body': Select(attrs={'required': True, 'class': 'form-control'}),
            'fuelType': Select(attrs={'required': True, 'class': 'form-control'}),
            'fuelRate': NumberInput(attrs={'required': True, 'class': 'form-control'}),
            'engineVolume': NumberInput(attrs={'required': True, 'class': 'form-control'}),
            'enginePower': NumberInput(attrs={'required': True, 'class': 'form-control'}),
            'gearbox': Select(attrs={'required': True, 'class': 'form-control'}),
            'year': DateInput(attrs={'required': True, 'class': 'form-control'}),
        }
        labels = {
            'name': 'Бренд',
            'manufacturer': 'Производитель',
            'body': 'Кузов',
            'fuelType': 'Топливо',
            'fuelRate': 'Расход топлива',
            'engineVolume': 'Объем двигателя',
            'enginePower': 'Мощность двигателя',
            'gearbox': 'Коробка передач',
            'year': 'Год выпуска'
        }
        error_messages = {
            'year': {
                'invalid': 'Введите дату в формате ГГГГ-ММ-ДД'
            }
        }


class CreateManufacturer(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'
        widgets = {
            'brand': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'country': TextInput(attrs={'required': True, 'class': 'form-control'}),
        }
        labels = {
            'brand': 'Бренд',
            'country': 'Страна'
        }
