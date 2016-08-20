from rest_framework import serializers
from .models import Auto, Manufacturer, Warehouse, Orders, Buyer


class AutoSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(queryset=Manufacturer.objects.all())

    class Meta:
        model = Auto
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Warehouse
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    goods = serializers.SlugRelatedField(slug_field='name', read_only=True)
    buyer = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Orders
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
