from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from app import models
from . import serializers


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = models.CarBrand.objects.all()
    serializer_class = serializers.CarBrandSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
