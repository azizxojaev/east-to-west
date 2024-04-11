from django.shortcuts import render
from east_to_west.models import *
from .models import *
from django.http import JsonResponse
import requests
from environs import Env


env = Env()
env.read_env()


def tour_booking_page(request):
    contact = Contact.objects.first()
    departures = Departure.objects.all()

    get_adults = request.GET.get('adults', 1)
    get_children = request.GET.get('children', 0)
    get_babies = request.GET.get('babies', 0)

    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        babies = request.POST.get('babies')
        tour_class = request.POST.get('class')
        apiToken = env.str('API_TOKEN')
        chatID = env.str('CHAT_ID')
        apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

        try:
            response = requests.post(apiURL, json={'chat_id': chatID, 'text': f"#Заявка от {first_name} {last_name}\n\nЭмейл: {email}\nНомер телефона: {phone_number}\nВыезд: {departure}\nМесто назначения: {destination}\nДата: {date}\nПассажиры: {adults} взрослых, {children} детей, {babies} младенцев\nКласс: {tour_class}\n\n{message}"})
        except Exception as e:
            print(e)
        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
        'departures': departures,
        'passengers': [int(get_adults), int(get_children), int(get_babies)]
    }
    return render(request, 'tour-booking.html', context=context)
