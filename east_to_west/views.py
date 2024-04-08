from django.shortcuts import render
from .models import *
import requests
from environs import Env
from tours.models import *
from django.http import JsonResponse


env = Env()
env.read_env()


def home_page(request):
    contact = Contact.objects.first()
    our_gallery = OurGallery.objects.all()
    gallery = Gallery.objects.all()
    reviews = Review.objects.all()
    destinations = Destination.objects.all()
    tour_destinations = TourDestination.objects.all()
    tour_types = TourType.objects.all()
    tours = Tour.objects.all()[:4]

    context = {
        'contact': contact,
        'our_gallery': our_gallery,
        'gallery': gallery,
        'reviews': reviews,
        'reviews_range': range(5),
        'destinations': destinations,
        'tour_destinations': tour_destinations,
        'tour_types': tour_types,
        'tours': tours
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

    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        apiToken = env.str('API_TOKEN')
        chatID = env.str('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': f"#Вопрос от {name}\n\nЗаголовок: {title}\nЭмейл: {email}\nНомер телефона: {phone_number}\n\n{message}"})
        except Exception as e:
            print(e)
        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1]
    }
    return render(request, 'contact-us.html', context=context)


def blogs_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-grid.html', context=context)


def blog_detail_page(request):
    contact = Contact.objects.first()
    context = {'contact': contact}
    return render(request, 'blog-detail.html', context=context)