import django.core.exceptions

from . import models
from rest_framework import serializers


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('name', )


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(source='street.name')
    city = serializers.CharField(source='street.city.name')
    house = serializers.CharField()
    apartment_number = serializers.IntegerField()

    def create(self, validated_data):
        city, _ = models.City.objects.get_or_create(name=validated_data['street']['city']['name'])
        street, _ = models.Street.objects.get_or_create(city=city, name=validated_data['street']['name'])
        return models.Address.objects.get_or_create(street=street,
                                                    house=validated_data['house'],
                                                    apartment_number=validated_data['apartment_number'])[0]

    def update(self, instance, validated_data):
        self.create(validated_data)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = models.Customer
        fields = ('id', 'first_name', 'last_name', 'second_name', 'address')

    def create(self, validated_data):
        address = AddressSerializer().create(validated_data['address'])
        del validated_data['address']
        try:
            return models.Customer.objects.get(**validated_data)
        except django.core.exceptions.ObjectDoesNotExist:
            return models.Customer.objects.create(address=address, **validated_data)

    def update(self, instance, validated_data):
        address = AddressSerializer().create(validated_data['address'])
        del validated_data['address']
        try:
            customer = models.Customer.objects.get(**validated_data)
        except django.core.exceptions.ObjectDoesNotExist:
            return models.Customer.objects.create(address=address, **validated_data)
        customer.address = address
        customer.save()
        return customer


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = serializers.SlugRelatedField(slug_field="name",
                                                queryset=models.Manufacturer.objects.all())

    class Meta:
        model = models.CarBrand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer()

    class Meta:
        model = models.Car
        fields = '__all__'

