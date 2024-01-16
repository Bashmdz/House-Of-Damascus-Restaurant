from django.contrib import admin
from .models import Table, Guest, Booking
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('guest', 'table', 'date_time', 'status', 'is_cancelled')
    search_fields = ['guest__name', 'guest__email', 'guest__phone_number']
    list_filter = ('status', 'is_cancelled', 'created_on',)
    summernote_fields = ('additional_notes',)

# Register your models here.

admin.site.register(Table)
admin.site.register(Guest)

