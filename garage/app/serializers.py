from . import models
from rest_framework import serializers


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = ('name', )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Customer
        fields = ('first_name', 'last_name', 'second_name', 'address')


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    manufacturer = serializers.SlugRelatedField(slug_field="name",
                                                queryset=models.Manufacturer.objects.all())

    class Meta:
        model = models.CarBrand
        fields = '__all__'
