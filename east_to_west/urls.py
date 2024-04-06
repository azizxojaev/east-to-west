from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact-us/', contact_page, name='contact'),
    path('tours/', tours_page, name='tours'),
    path('tour-booking/', tour_booking_page, name='tour_booking'),
    path('tours/tour', tour_detail_page, name='tour_detail'),
    path('blogs', blogs_page, name='blogs'),
    path('blogs/blog', blog_detail_page, name='blog_detail'),
]
