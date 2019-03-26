# Generated by Django 2.0 on 2018-09-17 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0012_auto_20180914_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Declined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hired', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteWriters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_writers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_writers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hired',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hired', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hired_before', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hired', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShortListedBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortlisted_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shorted_listed_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='invitedwriters',
            name='invitees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitees', to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='invitedwriters',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_writers', to='customer.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.CharField(choices=[('Writing', 'Writing'), ('Editing', 'Editing'), ('Rewriting', 'Rewriting')], default='essay service', max_length=250),
        ),
        migrations.AddField(
            model_name='shortlistedbid',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shorted_listed_bid', to='customer.Order'),
        ),
        migrations.AddField(
            model_name='declined',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declined', to='customer.Order'),
        ),
    ]
