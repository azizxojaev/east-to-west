from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact-us.html')


def tours_page(request):
    return render(request, 'tour-grid.html')


def tour_detail_page(request):
    return render(request, 'tour-detail.html')


def tour_booking_page(request):
    return render(request, 'tour-booking.html')


def blogs_page(request):
    return render(request, 'blog-grid.html')


def blog_detail_page(request):
    return render(request, 'blog-detail.html')