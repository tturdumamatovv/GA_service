from django.shortcuts import render
from .models import ContactInfo


def index(request):
    contact_info = ContactInfo.objects.all()
    return render(request, 'index.html', {'contact_info': contact_info})


def about(request):
    return render(request, 'about-us.html')


def service(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contacts.html')
