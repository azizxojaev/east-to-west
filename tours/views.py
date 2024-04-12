from django.shortcuts import render
from east_to_west.models import *
from .models import *
from django.http import JsonResponse
from .utils import send_message


def tour_booking_page(request):
    contact = Contact.objects.first()
    departures = Departure.objects.all()

    get_adults = request.GET.get('adults', 1)
    get_children = request.GET.get('children', 0)
    get_babies = request.GET.get('babies', 0)

    if request.method == "POST":
        full_name = request.POST.get('full-name')
        phone_number = request.POST.get('tel')
        message = request.POST.get('message')
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        babies = request.POST.get('babies')
        tour_class = request.POST.get('class')

        send_message(f"#Заявка_на_тур от {full_name}\n\nНомер телефона: {phone_number}\nВыезд: {departure}\nМесто назначения: {destination}\nДата: {date}\nПассажиры: {adults} взрослых, {children} детей, {babies} младенцев\nКласс: {tour_class}\n\n{message}")
        
        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
        'departures': departures,
        'passengers': [int(get_adults), int(get_children), int(get_babies)]
    }
    return render(request, 'tour-booking.html', context=context)

def country_house_booking_page(request):
    contact = Contact.objects.first()
    country_houses = CountryHouse.objects.all()

    if request.method == "POST":
        country_house = request.POST.get('country_house')
        full_name = request.POST.get('full-name')
        phone_number = request.POST.get('tel')
        message = request.POST.get('message')
        date = request.POST.get('date')
        
        send_message(f"#Заявка_на_дачу от {full_name}\n\nДача: {country_house}\nНомер телефона: {phone_number}\nДата: {date}\n\n{message}")

        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
        'country_houses': country_houses
    }
    return render(request, 'country-house-booking.html', context=context)

def visa_booking_page(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        visa_rezidence = request.POST.get('visa_rezidence')
        visa_visiting = request.POST.get('visa_visiting')
        full_name = request.POST.get('full-name')
        phone_number = request.POST.get('tel')
        message = request.POST.get('message')
        
        send_message(f"#Заявка_на_визу от {full_name}\n\nСтрана пользователя: {visa_rezidence}\nСтрана для визы: {visa_visiting}\nНомер телефона: {phone_number}\n\n{message}")

        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
    }
    return render(request, 'visa-booking.html', context=context)

def umrah_booking_page(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        full_name = request.POST.get('full-name')
        phone_number = request.POST.get('tel')
        message = request.POST.get('message')
        date = request.POST.get('date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        babies = request.POST.get('babies')
        tour_class = request.POST.get('class')

        send_message(f"#Заявка_на_тур_в_умру от {full_name}\n\nНомер телефона: {phone_number}\nДата: {date}\nПассажиры: {adults} взрослых, {children} детей, {babies} младенцев\nКласс: {tour_class}\n\n{message}")

        return JsonResponse({'success': True})

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1],
    }
    return render(request, 'umrah-booking.html', context=context)

def country_houses_page(request):
    contact = Contact.objects.first()
    country_houses_obj = CountryHouse.objects.all()

    min_price = 0
    max_price = 0
    if country_houses_obj:
        min_price = country_houses_obj.order_by('price').first().price
        max_price = country_houses_obj.order_by('price').last().price

    country_houses = []
    for i in country_houses_obj:
        images = HouseImage.objects.filter(house=i)
        country_houses.append([i, images])

    # active_houses = {}
    # if request.GET.get('destination'):
    #     destination = TourDestination.objects.get(slug=request.GET.get('destination'))
    #     tours = tours.filter(destination=destination)
    #     active_tours['destination'] = request.GET.get('destination')
    # if request.GET.get('tour_type'):
    #     tour_type = TourType.objects.get(slug=request.GET.get('tour_type'))
    #     tours = tours.filter(type=tour_type)
    #     active_tours['tour_type'] = request.GET.get('tour_type')

    # if request.method == 'POST':
    #     destination = request.POST.get('destination')
    #     tour_type = request.POST.get('tour_type')
    #     price_from = int(request.POST.get('price_from'))
    #     price_to = int(request.POST.get('price_to'))

    #     if destination != 'all':
    #         destination = TourDestination.objects.get(slug=destination)
    #         tours = tours.filter(destination=destination)
    #     if tour_type != 'all':
    #         tour_type = TourType.objects.get(slug=tour_type)
    #         tours = tours.filter(type=tour_type)

    #     tours = tours.filter(price__gte=price_from, price__lte=price_to)

    #     return render(request, 'includes/tours.html', {'tours': tours})

    context = {
        'contact': contact,
        'country_houses': country_houses,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'tour-grid.html', context=context)


def country_house_detail_page(request, slug):
    contact = Contact.objects.first()
    country_house = CountryHouse.objects.get(slug=slug)
    country_video = country_house.video.split('"')[5]
    country_images = HouseImage.objects.filter(house=country_house)

    context = {
        'contact': contact,
        'country_house': country_house,
        'country_video': country_video,
        'country_images': country_images
    }
    return render(request, 'tour-detail.html', context=context)