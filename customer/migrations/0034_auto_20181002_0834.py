# Generated by Django 2.0 on 2018-10-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0033_auto_20181002_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalfiles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]