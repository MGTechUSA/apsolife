from django.contrib import admin

from .models import Service, Category, Contact, Testimonial

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Testimonial)