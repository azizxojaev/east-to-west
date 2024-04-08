from django.shortcuts import render
from east_to_west.models import *
from .models import *
from django.http import JsonResponse
import requests
from environs import Env


env = Env()
env.read_env()


def tours_page(request):
    contact = Contact.objects.first()
    tours = Tour.objects.all()
    destinations = TourDestination.objects.all()
    tour_types = TourType.objects.all()
    min_price = tours.order_by('price').first().price
    max_price = tours.order_by('price').last().price

    active_tours = {}
    if request.GET.get('destination'):
        destination = TourDestination.objects.get(slug=request.GET.get('destination'))
        tours = tours.filter(destination=destination)
        active_tours['destination'] = request.GET.get('destination')
    if request.GET.get('tour_type'):
        tour_type = TourType.objects.get(slug=request.GET.get('tour_type'))
        tours = tours.filter(type=tour_type)
        active_tours['tour_type'] = request.GET.get('tour_type')

    if request.method == 'POST':
        destination = request.POST.get('destination')
        tour_type = request.POST.get('tour_type')
        price_from = int(request.POST.get('price_from'))
        price_to = int(request.POST.get('price_to'))

        if destination != 'all':
            destination = TourDestination.objects.get(slug=destination)
            tours = tours.filter(destination=destination)
        if tour_type != 'all':
            tour_type = TourType.objects.get(slug=tour_type)
            tours = tours.filter(type=tour_type)

        tours = tours.filter(price__gte=price_from, price__lte=price_to)

        return render(request, 'includes/tours.html', {'tours': tours})

    context = {
        'contact': contact,
        'tours': tours,
        'destinations': destinations,
        'tour_types': tour_types,
        'min_price': min_price,
        'max_price': max_price,
        'active_tours': active_tours
    }
    return render(request, 'tour-grid.html', context=context)


def tour_detail_page(request, slug):
    contact = Contact.objects.first()
    tour = Tour.objects.get(slug=slug)

    context = {
        'contact': contact,
        'tour': tour
    }
    return render(request, 'tour-detail.html', context=context)


def tour_booking_page(request):
    contact = Contact.objects.first()
    destinations = Tour.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        print(request.POST.get('tour'))
        tour = Tour.objects.get(slug=request.POST.get('tour')).title
        message = request.POST.get('message')
        apiToken = env.str('API_TOKEN')
        chatID = env.str('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': f"#Заявка от {first_name, last_name}\n\nЭмейл: {email}\nНомер телефона: {phone_number}\nТур: {tour}\n\n{message}"})
        except Exception as e:
            print(e)
        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
        'destinations': destinations
    }
    return render(request, 'tour-booking.html', context=context)
