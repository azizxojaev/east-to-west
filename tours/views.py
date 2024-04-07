from django.shortcuts import render
from east_to_west.models import *
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize


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

    context = {
        'contact': contact,
        'google_map_url': contact.google_map_url.split('"')[1]
    }
    return render(request, 'tour-booking.html', context=context)
