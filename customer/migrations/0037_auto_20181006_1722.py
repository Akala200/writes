# Generated by Django 2.0 on 2018-10-07 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0036_auto_20181006_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='offer_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offer_id', to='customer.Order'),
        ),
    ]
