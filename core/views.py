from django.shortcuts import render
from django.contrib import messages

from .models import Service, Category, Testimonial
from .forms import ContactForm

def home(request):
    category_list = Category.objects.all().order_by("rank")
    context = {
        'testimonial_list': Testimonial.objects.all(),
        'category_list': category_list,
    }

    return render(request, "home.html", context)


def list_services(request, category_id):
    
    category = Category.objects.get(id=category_id)
    service_list = Service.objects.filter(category=category)
    context = {
        'service_list': service_list,
        'category': category,
    }
    return render(request, "list_services.html", context)


def services(request, service_id):
    service = Service.objects.get(id=service_id)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, "Thank you for reaching out!")

    context = {
        'service': service,
        'category_img': f"images/services/{service.name[0]}.jpg"
    }
    return render(request, f"service.html", context)


def contact_service(request, service_id):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, "Thank you for reaching out!")

    service = Service.objects.get(id=service_id)
    form = ContactForm(initial={'service':service})
    context = {
        'form': form,
    }
    return render(request, "contact_offer.html", context)


def about_us(request):
    return render(request, "about_us.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, "Thank you for reaching out!")

    form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "contact.html", context)
