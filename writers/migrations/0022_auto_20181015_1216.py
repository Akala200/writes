# Generated by Django 2.0 on 2018-10-15 19:16

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0021_bids_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bids',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20),
        ),
    ]