from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api
from .serializers import AccommodationBookingSerializer, AccommodationSerializer, AirportTrasferSerializer, BookingSerializer, CarSerializer, GuideBookingSerializer, GuideSerializer, HighlightSerializer, RentCarSerializer, CarBookingSerializer, BookingAccommodationSerializer,  AccommodationDetailSerializer

from .models import Accomodation, Cars, Guide, Highlights, RentCars, AccommodationDetails, BookingAccommodation
from api import serializers
# Create your views here.


@api_view(['GET'])
def ShowAccommodation(request):
    accommodation = Accomodation.objects.all()
    serializer = AccommodationSerializer(accommodation, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def BookHotel(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def BookingAccommodations(request):
    serializer = AccommodationBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def AccommodationBooking(request):
    serializer = BookingAccommodationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# @api_view(['GET'])
# def ShowAccommodationBooking(request):
#     accommodation = BookingAccommodation.objects.all()
#     serializer = BookingAccommodationSerializer(accommodation, many=True)
#     return Response(serializer.data)

@api_view(['GET'])
def ViewAccommodationBooking(request):
    accommodation = BookingAccommodation.objects.all()
    serializer = BookingAccommodationSerializer(accommodation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ShowAccommodationBooking(request):
    accommodation = BookingAccommodation.objects.all()
    serializer = AccommodationSerializer(accommodation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewAccommodation(request, pk):
    accommodation = Accomodation.objects.get(id=pk)
    serializer = AccommodationSerializer(accommodation, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def showAccommodationDetails(request, pk):
    accommodation = AccommodationDetails.objects.get(id=pk)
    serializer = AccommodationDetailSerializer(accommodation, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def ViewHighlights(request):
    highlights = Highlights.objects.all()
    serializer = HighlightSerializer(highlights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def HighlightDetails(request, pk):
    highlights = Highlights.objects.get(id=pk)
    serializer = HighlightSerializer(highlights, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def GuideDetails(request):
    guide = Guide.objects.all()
    serializer = GuideSerializer(guide, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def BookGuide(request):
    serializer = GuideBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def CarRent(request):
    cars = Cars.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def RentCar(request):
    cars = RentCars.objects.all()
    serializer = RentCarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CarBooking(request):
    serializer = CarBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def AirportBooking(request):
    serializer = AirportTrasferSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
