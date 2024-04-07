from django.shortcuts import render
from .models import *


def home_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'index.html', context=context)


def about_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'about.html', context=context)


def contact_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
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
    context = {'contact': contact}
    return render(request, 'tour-booking.html', context=context)


def blogs_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-grid.html', context=context)


def blog_detail_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-detail.html', context=context)