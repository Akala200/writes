# Generated by Django 2.0 on 2018-09-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0023_order_in_progress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='status',
            new_name='approved',
        ),
        migrations.AddField(
            model_name='wallet',
            name='declined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wallet',
            name='is_pending',
            field=models.BooleanField(default=False),
        ),
    ]
