from django.shortcuts import render
from django.views import generic
from .models import Booking

# Create your views here.

class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "booking_system/index.html"
    paginate_by = 6

def menu(request):
    return render(request, 'menu.html')