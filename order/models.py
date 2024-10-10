from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Cart(models.Model):
    pass


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=128, validators=[
      RegexValidator(
        regex=r'^\+?998?\d{9,13}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
      ),
    ], blank=True, null=True)
    email = models.EmailField()
    order_notes = models.TextField(blank=True, null=True)