from django.contrib import admin
from .models import Review, Reservation, Room
admin.site.register(Review)
admin.site.register(Reservation)
admin.site.register(Room)