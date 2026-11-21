import uuid

from django.db import models


def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{uuid.uuid4()}.{ext}'
    return f'products/{newfilename}'


CATEGORIES = [
    ('Food', 'Food Category'),
    ('Drinks', 'Drinks Category'),
    ('Cleaning', 'Cleaning Category'),
    ('Hardware', 'Hardware Category'),
]
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    pic = models.ImageField(upload_to=gen_unique_path, default='products/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True) # once during creation
    updated_at = models.DateTimeField(auto_now=True) # every time update happens
    class Meta:
        db_table = 'products'


# Run migrations- create or update tables
# The commands:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


# python manage.py createsuperuser - to create for ana admin site
# vania 12345678
