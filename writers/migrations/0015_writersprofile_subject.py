# Generated by Django 2.0 on 2018-09-26 13:47

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0014_auto_20180925_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='writersprofile',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Advertising', 'Advertising'), ('Aeronautics', 'Aeronautics'), ('African-American Studies', 'African-American Studies'), ('Agricultural Studies', 'Agricultural Studies'), ('Alternative Medicine', 'Alternative Medicine'), ('American History', 'American History'), ('American Literature', 'American Literature'), ('Anthropology', 'Anthropology'), ('Antique Literature', 'Antique Literature'), ('Application Essay', 'Application Essay'), ('Architecture', 'Architecture'), ('Art', 'Art'), ('Asian Literature', 'Asian Literature'), ('Asian Studies', 'Asian Studies'), ('Astronomy', 'Astronomy'), ('Aviation', 'Aviation'), ('Biology', 'Biology'), ('Business', 'Business'), ('Canadian Studies', 'Canadian Studies'), ('Case Study', 'Case Study'), ('Chemistry', 'Chemistry'), ('Communication Strategies', 'Communication Strategies'), ('Communications and Media', 'Communications and Media'), ('Company Analysis', 'Company Analysis'), ('Computer Science', 'Computer Science'), ('Creative Writing', 'Creative Writing'), ('Criminology', 'Criminology'), ('Dance', 'Dance'), ('Design Analysis', 'Design Analysis'), ('Drama', 'Drama'), ('E-Commerce', 'E-Commerce'), ('East European Studies', 'East European Studies'), ('Economics', 'Economics'), ('Education', 'Education'), ('Education Theories', 'Education Theories'), ('Engineering', 'Engineering'), ('English', 'English'), ('English Literature', 'English Literature'), ('Environmental Issues', 'Environmental Issues'), ('Ethics', 'Ethics'), ('Finance', 'Finance'), ('Geography', 'Geography'), ('Geology', 'Geology'), ('Healthcare', 'Healthcare'), ('History', 'History'), ('Holocaust', 'Holocaust'), ('International Affairs/Relations', 'International Affairs/Relations'), ('Internet', 'Internet'), ('Investment', 'Investment'), ('IT Management', 'IT Management'), ('Journalism', 'Journalism'), ('Latin-American Studies', 'Latin-American Studies'), ('Law', 'Law'), ('Legal Issues', 'Legal Issues'), ('Linguistics', 'Linguistics'), ('Literature', 'Literature'), ('Logistics', 'Logistics'), ('Management', 'Management'), ('Marketing', 'Marketing'), ('Mathematics', 'Mathematics'), ('Medicine and Health', 'Medicine and Health'), ('Movies', 'Movies'), (' Music', ' Music'), (' Native-American Studies', 'Native-American Studies'), ('Nature', 'Nature'), ('Nursing', 'Nursing'), ('Nutrition', 'Nutrition'), ('Painting', 'Painting'), ('Pedagogy', 'Pedagogy'), ('Pharmacology', 'Pharmacology'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Public Relations', ' Public Relations'), ('Religion and Theology', 'Religion and Theology'), ('Shakespeare Studies', 'Shakespeare Studies'), ('Sociology', 'Sociology'), ('Sport', 'Sport'), ('Teacher', 'Teacher'), ('Technology', 'Technology'), ('Theatre', 'Theatre'), ('Tourism', 'Tourism'), ('Trade', 'Trade'), ('Web design', 'Web design'), ('West European Studies', 'West European Studies'), ('Other', 'Other')], default='', max_length=1135),
            preserve_default=False,
        ),
    ]