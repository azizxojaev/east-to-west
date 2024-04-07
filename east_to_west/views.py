from django.shortcuts import render
from .models import *


def home_page(request):
    contact = Contact.objects.first()
    our_gallery = OurGallery.objects.all()
    gallery = Gallery.objects.all()
    reviews = Review.objects.all()
    destinations = Destination.objects.all()

    context = {
        'contact': contact,
        'our_gallery': our_gallery,
        'gallery': gallery,
        'reviews': reviews,
        'reviews_range': range(5),
        'destinations': destinations
    }
    return render(request, 'index.html', context=context)


def about_page(request):
    contact = Contact.objects.first()
    our_gallery = OurGallery.objects.all()
    gallery = Gallery.objects.all()
    reviews = Review.objects.all()

    context = {
        'contact': contact,
        'our_gallery': our_gallery,
        'gallery': gallery,
        'reviews': reviews,
        'reviews_range': range(5)
    }
    return render(request, 'about.html', context=context)


def contact_page(request):
    contact = Contact.objects.first()

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1]
    }
    return render(request, 'contact-us.html', context=context)


def tours_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'tour-grid.html', context=context)


def tour_detail_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'tour-detail.html', context=context)


def tour_booking_page(request):
    contact = Contact.objects.first()

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1]
    }
    return render(request, 'tour-booking.html', context=context)


def blogs_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-grid.html', context=context)


def blog_detail_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-detail.html', context=context)