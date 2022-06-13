from distutils.command.upload import upload
import email
from statistics import mode
from django.db import models

# Create your models here.


class Accomodation(models.Model):
    Accommodation_name = models.CharField(max_length=200)
    Accommodation_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Accommodation_name


class AccommodationDetails(models.Model):
    Accommodation_name = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    image4 = models.ImageField(upload_to='images/')
    image5 = models.ImageField(upload_to='images/')
    image6 = models.ImageField(upload_to='images/')
    image7 = models.ImageField(upload_to='images/')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return ("Accommodation details added successfully.")


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    def __str__(self):
        return ("Booking has been done successfully")


class AccommodationBooking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    check_in = models.CharField(max_length=200)
    check_out = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()

    def __str__(self):
        return ("Accommodation has been booked successfully")


class BookingAccommodation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    check_in = models.CharField(max_length=200)
    check_out = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    accommodation_name = models.CharField(max_length=200)

    def __str__(self):
        return ("Accommodation has been booked successfully")


class Highlights(models.Model):
    sparkling_clean = models.BooleanField()
    front_desk = models.BooleanField()
    airport_transfer = models.BooleanField()
    free_wifi = models.BooleanField()
    sauna = models.BooleanField()

    def __str__(self):
        return("Highlights added successfully!")


class Guide(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    available = models.BooleanField()
    rating = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return("Tourist guide added successfully")


class GuideBooking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)

    def __str__(self):
        return ("Guide has been booked successfully")


class Cars(models.Model):
    name = models.CharField(max_length=200)
    seats = models.IntegerField()
    large_bag = models.IntegerField()
    small_bag = models.IntegerField()
    mileage = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return ("New Car added successfully")


class RentCars(models.Model):
    name = models.CharField(max_length=200)
    seats = models.IntegerField()
    large_bag = models.IntegerField()
    small_bag = models.IntegerField()
    mileage = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return ("New Car added successfully")


class CarBooking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    no_of_travellers = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return ("Car has been booked successfully")


class AirportTrasfer(models.Model):
    pick_up = models.CharField(max_length=200)
    drop_off = models.CharField(max_length=200)
    no_of_travellers = models.IntegerField()
    pick_up_date = models.CharField(max_length=200)
    pck_up_time = models.CharField(max_length=100)

    def __str__(self):
        return ("Airport transger has been booked successfully")
