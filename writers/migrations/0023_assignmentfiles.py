# Generated by Django 2.0 on 2018-10-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0022_auto_20181015_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_file', models.FileField(upload_to='download_assignment')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writers.Bids')),
            ],
        ),
    ]
