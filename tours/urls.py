from django.urls import path
from .views import *


urlpatterns = [
    path('tour-booking/', tour_booking_page, name='tour_booking'),
    path('country-houses/', country_houses_page, name='country_houses'),
    path('country-houses/<str:slug>', country_house_detail_page, name='country_house_detail'),
    path('country-house-booking/', country_house_booking_page, name='country_house_booking'),
    path('visa-booking/', visa_booking_page, name='visa_booking'),
    path('umrah-booking/', umrah_booking_page, name='umrah_booking'),
]