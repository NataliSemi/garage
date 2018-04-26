from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Street(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'city')


class Address(models.Model):
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10, verbose_name="House number")
    apartment_number = models.PositiveSmallIntegerField(verbose_name='Apartment number')

    class Meta:
        unique_together = ('street', 'house', 'apartment_number')


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)


class CarBrand(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)

    class Meta:
        unique_together = ('manufacture', 'model')


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10)
    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)


class Floor(models.Model):
    name = models.CharField(max_length=15, verbose_name='Floor name')


class Rent(models.Model):
    tenant = models.ForeignKey('Customer', on_delete=models.CASCADE)
    start = models.DateField(verbose_name='Start rent date')
    finish = models.DateField(verbose_name='Finish rent date')


class Box(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(verbose_name='Box number')
    owner = models.ForeignKey('Customer', on_delete=models.CASCADE)
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)


class Customer(models.Model):
    fist_name = models.CharField(max_length=50, verbose_name="first name of customer")
    last_name = models.CharField(max_length=50, verbose_name="last name of customer")
    second_name = models.CharField(max_length=50, verbose_name="second name of customer")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
