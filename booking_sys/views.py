from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm

# Create your views here.

class BookingList(generic.ListView):
    queryset = Booking.objects.all()
    template_name = "booking_sys/index.html"
    paginate_by = 6

def menu(request):
    return render(request, 'menu.html')

    class BookFormView(generic.CreateView):
        """
        View to create a new booking
        """
    model = Booking
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = reverse_lazy('bookinglist')

    def form_valid(self, form):
        form.instance.contact_id = self.request.user.id
        messages.success(self.request, 'Booking submitted successfully')
        return super().form_valid(form)


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
    form_class = BookingForm
    template_name = 'bookingform.html'
    success_url = reverse_lazy('bookinglist')

    def test_func(self):
        return self.request.user.id == self.get_object().contact_id

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
        return self.request.user.id == self.get_object().contact_id

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking deleted successfully')
        return super().delete(request, *args, **kwargs)