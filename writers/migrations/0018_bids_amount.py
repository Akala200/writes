# Generated by Django 2.0 on 2018-10-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0017_auto_20181001_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]