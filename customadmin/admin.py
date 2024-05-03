from django.contrib import admin


# Custom Admin Registration.
from core.models import Service, Offer, Contact, Testimonial

class Table:
    def __init__(self, name, model, fields=None, order_by=None) -> None:
        self.name = name
        self.model = model
        self.fields = fields
        self.order_by = order_by

models = [
    Table(
        name="Service",
        model=Service,
        order_by = ["rank"],
    ),
    Table(
        name="Offer",
        model=Offer, 
        fields = ["service", "name", "price"]
    ),
    Table(
        name="Contact",
        model=Contact,
        fields=["full_name", "email", "phone"],
        # order_by=["level", "subject"]
    ),
    Table(
        name="Testimonial",
        model=Testimonial,
        # fields=["test", "question", "is_public"],
        # order_by=["level", "subject"]
    ),
]