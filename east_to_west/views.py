from django.shortcuts import render
from .models import *
import requests
from environs import Env
from tours.models import *
from django.http import JsonResponse
from tours.utils import send_message


env = Env()
env.read_env()


def home_page(request):
    context = {
        'contact': Contact.objects.first(),
        'our_gallery': OurGallery.objects.all(),
        'gallery': Gallery.objects.all(),
        'reviews': Review.objects.all(),
        'reviews_range': range(5),
        'departures': Departure.objects.all(),
    }

    return render(request, 'index.html', context=context)


def about_page(request):
    context = {
        'contact': Contact.objects.first(),
        'our_gallery': OurGallery.objects.all(),
        'gallery': Gallery.objects.all(),
        'reviews': Review.objects.all(),
        'reviews_range': range(5)
    }
    return render(request, 'about.html', context=context)


def contact_page(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        message = request.POST.get('message')

        send_message(f"#Вопрос от {name}\n\nЗаголовок: {title}\nЭмейл: {email}\nНомер телефона: {tel}\n\n{message}")

        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1]
    }
    return render(request, 'contact-us.html', context=context)