# Generated by Django 2.0 on 2018-10-11 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0018_bids_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
