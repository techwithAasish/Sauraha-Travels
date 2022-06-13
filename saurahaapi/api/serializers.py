from dataclasses import fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import Accomodation, AirportTrasfer, Booking, Cars, Guide, GuideBooking, Highlights, RentCars, CarBooking, AccommodationBooking, AccommodationDetails, BookingAccommodation


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = '__all__'


class AccommodationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationDetails
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class AccommodationBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationBooking
        fields = '__all__'


class BookingAccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingAccommodation
        fields = '__all__'


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlights
        fields = '__all__'


class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class GuideBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideBooking
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class RentCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentCars
        fields = '__all__'


class CarBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBooking
        fields = '__all__'


class AirportTrasferSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportTrasfer
        fields = '__all__'
