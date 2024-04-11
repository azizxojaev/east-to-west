from django.urls import path
from .views import *


urlpatterns = [
    path('tour-booking/', tour_booking_page, name='tour_booking'),
    path('country-houses/', country_houses_page, name='country_houses'),
    path('tours/<str:slug>', country_house_detail_page, name='country_house_detail'),
]