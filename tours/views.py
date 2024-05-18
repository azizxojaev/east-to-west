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
    country_houses_obj = CountryHouse.objects.all()

    country_houses = [(house, HouseImage.objects.filter(house=house)) for house in country_houses_obj]

    context = {
        'contact': Contact.objects.first(),
        'country_houses': country_houses
    }
    return render(request, 'tour-grid.html', context=context)


def country_house_detail_page(request, slug):
    country_house = CountryHouse.objects.get(slug=slug)

    context = {
        'contact': Contact.objects.first(),
        'country_house': country_house,
        'country_video': country_house.video.split('"')[5],
        'country_images': HouseImage.objects.filter(house=country_house)
    }
    return render(request, 'tour-detail.html', context=context)


def create_country_house_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        capacity = request.POST.get('capacity')
        distance = request.POST.get('distance')
        rooms = request.POST.get('rooms')
        pools = request.POST.get('pools')
        bathrooms = request.POST.get('bathrooms')
        tv = request.POST.get('tv') == 'on'
        have_playstation = request.POST.get('have_playstation') == 'on'
        have_karaoke = request.POST.get('have_karaoke') == 'on'
        have_tenis = request.POST.get('have_tenis') == 'on'
        have_tapchan = request.POST.get('have_tapchan') == 'on'
        have_living_room = request.POST.get('have_living_room') == 'on'
        have_outdoor_kitchen = request.POST.get('have_outdoor_kitchen') == 'on'
        have_indoor_kitchen = request.POST.get('have_indoor_kitchen') == 'on'
        have_sauna = request.POST.get('have_sauna') == 'on'
        have_terrace = request.POST.get('have_terrace') == 'on'
        have_barbeque = request.POST.get('have_barbeque') == 'on'
        have_jacuzzi = request.POST.get('have_jacuzzi') == 'on'
        have_conditioners = request.POST.get('have_conditioners') == 'on'
        have_wifi = request.POST.get('have_wifi') == 'on'
        have_football_pitch = request.POST.get('have_football_pitch') == 'on'
        have_projector = request.POST.get('have_projector') == 'on'
        have_fridge = request.POST.get('have_fridge') == 'on'
        smoking = request.POST.get('smoking') == 'on'
        alcohol = request.POST.get('alcohol') == 'on'
        pets = request.POST.get('pets') == 'on'
        events = request.POST.get('events') == 'on'
        children = request.POST.get('children') == 'on'

        message = f"""#Заявка на сотрудничество :\n\nИмя: {name}\nНомер телефона: {phone_number}\nЛокация: {location}\nВместимость: {capacity}\nРасстояние от города: {distance}\nКомнаты: {rooms}\nБассейны: {pools}\nВанные комнаты: {bathrooms}\nНаличие ТВ: {'Да' if tv else 'Нет'}\nНаличие PlayStation: {'Да' if have_playstation else 'Нет'}\nНаличие Караоке: {'Да' if have_karaoke else 'Нет'}\nНаличие Тенниса: {'Да' if have_tenis else 'Нет'}\nНаличие Тапчана: {'Да' if have_tapchan else 'Нет'}\nНаличие Гостиной: {'Да' if have_living_room else 'Нет'}\nНаличие Летней кухни: {'Да' if have_outdoor_kitchen else 'Нет'}\nНаличие Внутренней кухни: {'Да' if have_indoor_kitchen else 'Нет'}\nНаличие Сауны: {'Да' if have_sauna else 'Нет'}\nНаличие Террасы: {'Да' if have_terrace else 'Нет'}\nНаличие Барбекю: {'Да' if have_barbeque else 'Нет'}\nНаличие Джакузи: {'Да' if have_jacuzzi else 'Нет'}\nНаличие Кондиционеров: {'Да' if have_conditioners else 'Нет'}\nНаличие WiFi: {'Да' if have_wifi else 'Нет'}\nНаличие Футбольного поля: {'Да' if have_football_pitch else 'Нет'}\nНаличие Проектора: {'Да' if have_projector else 'Нет'}\nНаличие Холодильника: {'Да' if have_fridge else 'Нет'}\nРазрешено курение: {'Да' if smoking else 'Нет'}\nРазрешён алкоголь: {'Да' if alcohol else 'Нет'}\nРазрешены домашние животные: {'Да' if pets else 'Нет'}\nРазрешены мероприятия: {'Да' if events else 'Нет'}\nРазрешены дети: {'Да' if children else 'Нет'}"""

        send_message(message)

        return JsonResponse({'success': True})

    context = {
        'contact': Contact.objects.first()
    }
    return render(request, 'create-country-house.html', context=context)