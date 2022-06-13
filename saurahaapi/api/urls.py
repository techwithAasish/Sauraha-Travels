from unicodedata import name
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('hotels/list', views.ShowAccommodation, name="hotel-list"),
    path('bookHotel/', views.BookHotel, name="book -hotels"),
    path('bookAccommodation/', views.BookingAccommodations,
         name="book-Accommodation"),
    path('accommodationBooking/', views.AccommodationBooking,
         name='accommodation booking'),
    path('accommodationBooking/list/', views.ViewAccommodationBooking,
         name='accommodationbooking list'),
    path('accommodation-detail/<int:pk>/',
         views.ViewAccommodation, name='Accommodation detail'),
    path('accommodation/<int:pk>/',
         views.showAccommodationDetails, name='accommodation'),
    path('highlights/', views.ViewHighlights, name="view highlights"),
    path('highlight-details/<int:pk>/',
         views.HighlightDetails, name='highlight details'),
    path('viewGuides/', views.GuideDetails, name="View Guides"),
    path('bookGuide/', views.BookGuide, name='book-guide'),
    path('rentCar/', views.CarRent, name='Car rent'),
    path('viewCars/', views.RentCar, name='view cars'),
    path('bookCar/', views.CarBooking, name='book-car'),
    path('bookAirportTrasfer/', views.AirportBooking, name='book-airportTrasfer'),
]
