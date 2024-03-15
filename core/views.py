from django.shortcuts import render
from django.contrib import messages

from .models import Service, Offer
from .forms import ContactForm

def home(request):
    service_list = Service.objects.all().order_by("rank")
    context = {
        'service_list': service_list,
    }    
    return render(request, "home.html", context)


def offer(request, service_id):
    
    service = Service.objects.get(id=service_id)
    offer_list = Offer.objects.filter(service=service)
    context = {
        'offer_list': offer_list,
    }
    return render(request, "offers.html", context)

def contact(request, offer_id):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

        messages.success(request, "Thank you for reaching out!")

    offer = Offer.objects.get(id=offer_id)
    form = ContactForm(initial={'offer':offer})
    context = {
        'form': form,
    }
    return render(request, "contact.html", context)
