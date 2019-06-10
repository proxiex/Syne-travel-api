from django.contrib import admin
from .models import Flight, Airline, Booking

# Register your models here.

admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Airline)
