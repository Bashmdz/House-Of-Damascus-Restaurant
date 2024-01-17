# from django.contrib import admin
# from .models import Table, Guest, Booking
# from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Booking)
# class BookingAdmin(SummernoteModelAdmin):
#     list_display = ('guest', 'table', 'date_time', 'status', 'is_cancelled')
#     search_fields = ['guest__name', 'guest__email', 'guest__phone_number']
#     list_filter = ('status', 'is_cancelled', 'created_on',)
#     summernote_fields = ('additional_notes',)

from django.contrib import admin
from .models import Booking, Guest
from django_summernote.admin import SummernoteModelAdmin

class BookingAdmin(SummernoteModelAdmin):
    list_display = ('user', 'date', 'time', 'guests', 'status')
    search_fields = ['user__username', 'user__email']
    list_filter = ('status',)
    date_hierarchy = 'date'

admin.site.register(Booking)
admin.site.register(Guest)

