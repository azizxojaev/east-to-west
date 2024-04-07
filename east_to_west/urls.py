from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact-us/', contact_page, name='contact'),
    path('blogs', blogs_page, name='blogs'),
    path('blogs/blog', blog_detail_page, name='blog_detail'),
]
