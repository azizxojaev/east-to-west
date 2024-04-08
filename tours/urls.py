from django.urls import path
from .views import *


urlpatterns = [
    path('tour-booking/', tour_booking_page, name='tour_booking'),
]