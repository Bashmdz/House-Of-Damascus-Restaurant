# Generated by Django 5.0.1 on 2024-01-20 20:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_sys', '0006_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='group',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
