from django.contrib import admin

# Register your models here.
from .models import Product, ContactDetails

admin.site.register(Product)
admin.site.register(ContactDetails)