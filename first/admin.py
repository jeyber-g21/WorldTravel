from django.contrib import admin

from .models import User,Continents,Travel,Month,Booking
# Register your models here.
admin.site.register(User)
admin.site.register(Month)
admin.site.register(Continents)
admin.site.register(Travel)
admin.site.register(Booking)
