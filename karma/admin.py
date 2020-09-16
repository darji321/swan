from django.contrib import admin
from .models import Addresses,Profile,Products,Coming_Products
# Register your models here.
admin.site.register(Addresses)
admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Coming_Products)