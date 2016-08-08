from django.forms import ModelForm, TextInput, Select, NumberInput, DateInput, EmailInput
from .models import Manufacturer, Auto, Buyer, Orders


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


class CreateBuyer(ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'lastname': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'email': EmailInput(attrs={'required': True, 'class': 'form-control'}),
            'phone': TextInput(attrs={'required': True, 'class': 'form-control', 'placeholder': 'Формат номера: 0ХХ 123-45-67'}),
        }
        labels = {
            'name': 'Имя',
            'lastname': 'Фамилия',
            'email': 'Email',
            'phone': 'Мобильный телефон'
        }


class CreateOrders(ModelForm):
    class Meta:
        model = Orders
        fields = ['goods', 'amount', 'buyer']
