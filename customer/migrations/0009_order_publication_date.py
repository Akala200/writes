# Generated by Django 2.0 on 2018-09-13 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20180913_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
