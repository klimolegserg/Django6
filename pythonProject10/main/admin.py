from django.contrib import admin

# Register your models here.
from main.models import Client, Car, Sale


admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Sale)
