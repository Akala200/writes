# Generated by Django 2.0 on 2018-09-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20180910_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletbalance',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=1000, null=True),
        ),
    ]
