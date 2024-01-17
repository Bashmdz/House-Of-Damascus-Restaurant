from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Guest: {self.name} | Email: {self.email} | Phone: {self.phone_number}"


class Booking(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    )

    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    is_cancelled = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.guest} - {self.date_time}"

    class Meta:
        ordering = ["created_on"]


# class Booking(models.Model):
#         STATUS_CHOICES = (
#         ("Pending", "Pending"),
#         ("Confirmed", "Confirmed"),
#         ("Cancelled", "Cancelled"),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()
#     guests = models.IntegerField()

#     def __str__(self):
#         return f"{self.user.username} - {self.date} {self.time}"

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Booking for {self.guest.name} | Table: {self.table.number} | Status: {self.status}"