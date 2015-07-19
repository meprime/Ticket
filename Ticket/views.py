from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact.html')


def user_tickets(request):
    return render(request, 'user_tickets.html')
