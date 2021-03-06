# Generated by Django 2.0 on 2018-09-17 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20180917_1541'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('writers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='writer_bids',
        ),
        migrations.AddField(
            model_name='bids',
            name='bidders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bids',
            name='bidding_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_order', to='customer.Order'),
        ),
    ]
