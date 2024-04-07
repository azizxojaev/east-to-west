from django.urls import path
from .views import *


urlpatterns = [
    path('tours/', tours_page, name='tours'),
    path('tour-booking/', tour_booking_page, name='tour_booking'),
    path('tours/<str:slug>', tour_detail_page, name='tour_detail'),
]