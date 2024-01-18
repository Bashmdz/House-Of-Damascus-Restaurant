from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import Booking
from .forms import ReservationForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "booking_sys/index.html"
    paginate_by = 6

def menu(request):
    return render(request, 'menu.html')

class BookFormView(SuccessMessageMixin, generic.CreateView):
    """
    View to create a new booking
    """
    model = Booking
    form_class = ReservationForm
    template_name = 'bookingform.html'
    success_url = reverse_lazy('bookinglist')
    success_message = 'Booking submitted successfully'

    def form_valid(self, form):
        # Check if a booking already exists for the selected date and time
        existing_booking = Booking.objects.filter(date=form.cleaned_data['date'], time=form.cleaned_data['time']).first()
        if existing_booking:
            messages.error(self.request, 'Booking for the selected date and time already exists.')
            return self.form_invalid(form)

        form.instance.guest = self.request.user
        messages.success(self.request, 'Booking submitted successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Add this to print validation errors if the form is invalid
        print(form.errors)
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # Print or log the form data
            print(form.cleaned_data)
        return super().post(request, *args, **kwargs)

class BookListView(generic.ListView):
    """
    View to display bookings already made by a user
    """
    model = Booking
    queryset = Booking.objects.order_by('date')
    template_name = 'bookinglist.html'

class BookUpdateView(UserPassesTestMixin, generic.UpdateView):
    """
    View to allow a booking to be updated
    """
    model = Booking
    form_class = ReservationForm
    template_name = 'bookingform.html'
    success_url = reverse_lazy('bookinglist')

    def test_func(self):
        return self.request.user.id == self.get_object().guest.id

    def form_valid(self, form):
        form.instance.status = 0
        messages.success(self.request, 'Booking updated successfully')
        return super().form_valid(form)

class BookDeleteView(UserPassesTestMixin, generic.DeleteView):
    """
    View to allow deletion of a booking
    """
    model = Booking
    template_name = 'bookingdelete.html'
    success_url = reverse_lazy('bookinglist')

    def test_func(self):
        return self.request.user.id == self.get_object().guest.id

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking deleted successfully')
        return super().delete(request, *args, **kwargs)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
