# Generated by Django 2.0 on 2018-09-10 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_auto_20180910_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('balance_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_balance', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='balance',
        ),
    ]