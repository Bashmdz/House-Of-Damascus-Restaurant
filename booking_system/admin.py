from django.contrib import admin
from .models import Table, Guest, Booking, MenuItem

# Register your models here.

admin.site.register(Table)
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(MenuItem)
