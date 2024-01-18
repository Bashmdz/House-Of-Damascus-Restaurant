from django import forms
from .models import Booking
import datetime

class ReservationForm(forms.ModelForm):
    """
    Booking form for user reservations
    """
    class Meta:
        model = Booking
        fields = ('date', 'time', 'group', 'status')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        selected_date = cleaned_data.get('date')
        selected_time = cleaned_data.get('time')

        # Ensure reservations are made for tomorrow or later
        if selected_date and selected_date <= datetime.date.today():
            raise forms.ValidationError("Reservations must be made for tomorrow or a future date")

        # Check for existing bookings on the selected date and time
        existing_bookings = Booking.objects.filter(date=selected_date, time=selected_time)
        if existing_bookings.exists():
            raise forms.ValidationError("This time slot is not available. Please choose a different date or time.")

        return cleaned_data

    def clean_time(self):
        selected_time = self.cleaned_data['time']
        if selected_time not in [choice[0] for choice in Booking.TIME_CHOICES]:
            raise forms.ValidationError("Select a valid choice for time")

        return selected_time
