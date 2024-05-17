from django.db import models
from cloudinary.models import CloudinaryField


# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     image = CloudinaryField('apsolife_images/')

#     def __str__(self) -> str:
#         return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="images/")
    image = CloudinaryField('apsolife_images/')
    # description = models.TextField()
    rank = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    image = CloudinaryField('apsolife_images/', blank=True)

    category = models.ForeignKey("core.Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    bullet_points = models.TextField()
    
    def get_bullet_points(self):
        return self.bullet_points.split("\n")

    def __str__(self) -> str:
        return f"{self.category} / {self.name}"
    

class Contact(models.Model):

    CONTACT_METHOD_CHOICES = (
        ("CALL", "Call"),
        ("WHATSAPP", "WhatsApp"),
        ("EMAIL", "Email"),
    )
    
    service = models.ForeignKey("core.Service", on_delete=models.CASCADE)

    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    message = models.TextField()

    contact_method = models.CharField(choices=CONTACT_METHOD_CHOICES, max_length=50)
    def __str__(self):
        return f"{self.full_name}"

    
class Testimonial(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    full_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.full_name
