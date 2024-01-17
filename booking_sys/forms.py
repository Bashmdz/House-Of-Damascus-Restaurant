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

    def clean_date(self):
        selected_date = self.cleaned_data['date']

        # Ensure reservations are made for tomorrow or later
        if selected_date <= datetime.date.today():
            raise forms.ValidationError(
                "Reservations must be made for tomorrow or a future date")

        return selected_date

    def clean_time(self):
        selected_time = self.cleaned_data['time']

        # Define restaurant operating hours
        opening_time, closing_time = datetime.time(9, 0), datetime.time(21, 0)

        # Check if the selected time is within operating hours
        if not opening_time <= selected_time <= closing_time:
            raise forms.ValidationError(
                "The restaurant operates from 9 am to 9 pm every day. Please choose a valid time.")

        return selected_time
