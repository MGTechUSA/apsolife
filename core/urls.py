
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list_services/<str:category_id>/', views.list_services, name="list_services"),
    path('contact_service/<str:service_id>', views.contact_service, name="contact_service"),

    # Services URL
    path('services/<str:service_id>/', views.services, name="services"),

    # About us URL
    path('about_us/', views.about_us, name="about_us"),

    # Contact URL
    path('contact/', views.contact, name="contact"),
    
    # # List Services URL
    # path('list_services/<str:category>/', views.list_services, name="list_services"),

    # # Services URL
    # path('services/<str:service_id>/', views.services, name="services"),

    # # About us URL
    # path('about_us/', views.about_us, name="about_us"),

    # # Contact URL
    # path('contact/', views.contact, name="contact"),
    # path('contact_specific_service/<str:service_id>', views.contact_specific_service, name="contact_specific_service"),

    # path('careers/', views.careers, name="careers"),
    # path('careers/<str:career_id>', views.checkout_career, name="careers"),

]
