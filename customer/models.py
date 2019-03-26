from decimal import Decimal

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MinLengthValidator

from .utils import invite_writer



class Wallet(models.Model):
    wallet_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    is_pending = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    credit = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.wallet_id)


class WalletBalance(models.Model):
    balance_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name='wallet_balance'
    )
    balance = models.DecimalField(decimal_places=2, max_digits=20, default=Decimal('0.00'))

    def __str__(self):
        return str(self.balance_id)


class Order(models.Model):
    order_type = (
        ('Essay (any type)', 'Essay (any type)'),
        ('Admission Essay', 'Admission Essay'),
        ('Annotated Bibliography', 'Annotated Bibliography'),
        ('Article Review', 'Article Review'),
        ('Book / Movie Review', 'Book / Movie Review'),
        ('Business Plan', 'Business Plan'),
        ('Case Study', 'Case Study'),
        ('Coursework', 'Coursework'),
        ('Creative Writing', 'Creative Writing'),
        ('Critical Thinking / Review', 'Critical Thinking / Review'),
        ('Literature Review', 'Literature Review'),
        ('Multiple choice question', 'Multiple choice question'),
        ('Presentation or Speech', 'Presentation or Speech'),
        ('Reflective Writing', 'Reflective Writing'),
        ('Report', 'Report'),
        ('Research Paper', 'Research Paper'),
        ('Research Proposal', 'Research Proposal'),
        ('Term Paper', 'Term Paper')
    )

    
    service_choice = (
        ('Writing', 'Writing'),
        ('Editing', 'Editing'),
        ('Rewriting', 'Rewriting')

    )

    source_choice = (
        ('0 source','0 source'),
        ('1 source', '1 source'),
        ('2 source', '2 source'),
        ('3 source', '3 source'),
        ('4 source', '4 source'),
        ('5 source', '5 source'),
        ('6 source', '6 source'),
        ('8 source', '8 source'),
        ('9 source', '9 source'),
        ('10 source', '10 source'),
        ('11 source', '11 source'),
        ('12 source', '12 source'),
        ('13 source', '13 source'),
        ('14 source', '14 source'),
        ('15 source', '15 source'),
        ('16 source', '16 source'),
        ('17 source', '17 source'),
        ('18 source', '18 source'),
        ('19 source', '19 source'),
        ('20 source', '20 source'),
        ('21 source', '21 source'),
        ('22 source', '22 source'),
        ('23 source', '23 source'),
        ('24 source', '24 source'),
        ('25 source', '25 source'),
        ('26 source', '26 source'),
        ('27 source', '27 source'),
        ('28 source', '28 source'),
        ('29 source', '29 source'),
        ('39 source', '30 source')


    )

    style_choice = (
        ('Harvard', 'Harvard'),
        (' APA', ' APA'),
        ('Chicago/Turabian', 'Chicago/Turabian'),
        ('Not Applicable', 'Not Applicable'),
        (' Other', ' Other')
    )

    subject_choice = (
        ('Advertising', 'Advertising'),
        ('Aeronautics', 'Aeronautics'),
        ('African-American Studies', 'African-American Studies'),
        ('Agricultural Studies', 'Agricultural Studies'),
        ('Alternative Medicine', 'Alternative Medicine'),
        ('American History', 'American History'),
        ('American Literature', 'American Literature'),
        ('Anthropology', 'Anthropology'),
        ('Antique Literature', 'Antique Literature'),
        ('Application Essay', 'Application Essay'),
        ('Architecture', 'Architecture'),
        ('Art', 'Art'),
        ('Asian Literature', 'Asian Literature'),
        ('Asian Studies', 'Asian Studies'),
        ('Astronomy', 'Astronomy'),
        ('Aviation', 'Aviation'),
        ('Biology', 'Biology'),
        ('Business', 'Business'),
        ('Canadian Studies', 'Canadian Studies'),
        ('Case Study', 'Case Study'),
        ('Chemistry', 'Chemistry'),
        ('Communication Strategies', 'Communication Strategies'),
        ('Communications and Media', 'Communications and Media'),
        ('Company Analysis', 'Company Analysis'),
        ('Computer Science', 'Computer Science'),
        ('Creative Writing', 'Creative Writing'),
        ('Criminology', 'Criminology'),
        ('Dance', 'Dance'),
        ('Design Analysis', 'Design Analysis'),
        ('Drama', 'Drama'),
        ('E-Commerce', 'E-Commerce'),
        ('East European Studies', 'East European Studies'),
        ('Economics', 'Economics'),
        ('Education', 'Education'),
        ('Education Theories', 'Education Theories'),
        ('Engineering', 'Engineering'),
        ('English', 'English'),
        ('English Literature', 'English Literature'),
        ('Environmental Issues', 'Environmental Issues'),
        ('Ethics', 'Ethics'),
        ('Finance', 'Finance'),
        ('Geography', 'Geography'),
        ('Geology', 'Geology'),
        ('Healthcare', 'Healthcare'),
        ('History', 'History'),
        ('Holocaust', 'Holocaust'),
        ('International Affairs/Relations', 'International Affairs/Relations'),
        ('Internet', 'Internet'),
        ('Investment', 'Investment'),
        ('IT Management', 'IT Management'),
        ('Journalism', 'Journalism'),
        ('Latin-American Studies', 'Latin-American Studies'),
        ('Law', 'Law'),
        ('Legal Issues', 'Legal Issues'),
        ('Linguistics', 'Linguistics'),
        ('Literature', 'Literature'),
        ('Logistics', 'Logistics'),
        ('Management', 'Management'),
        ('Marketing', 'Marketing'),
        ('Mathematics', 'Mathematics'),
        ('Medicine and Health', 'Medicine and Health'),
        ('Movies', 'Movies'),
        (' Music', ' Music'),
        (' Native-American Studies', 'Native-American Studies'),
        ('Nature', 'Nature'),
        ('Nursing', 'Nursing'),
        ('Nutrition', 'Nutrition'),
        ('Painting', 'Painting'),
        ('Pedagogy', 'Pedagogy'),
        ('Pharmacology', 'Pharmacology'),
        ('Philosophy', 'Philosophy'),
        ('Physics', 'Physics'),
        ('Political Science', 'Political Science'),
        ('Psychology', 'Psychology'),
        ('Public Relations', ' Public Relations'),
        ('Religion and Theology', 'Religion and Theology'),
        ('Shakespeare Studies', 'Shakespeare Studies'),
        ('Sociology', 'Sociology'),
        ('Sport', 'Sport'),
        ('Teacher', 'Teacher'),
        ('Technology', 'Technology'),
        ('Theatre', 'Theatre'),
        ('Tourism', 'Tourism'),
        ('Trade', 'Trade'),
        ('Web design', 'Web design'),
        ('West European Studies', 'West European Studies'),
        ('Other', 'Other')

    )

    level_choice = (
        ('School', 'School'),
        ('University', 'University'),
        ('Dictorate', 'Dictorate'),
    )
    page_choice = (
        ('1 page / 275 words', '1 page / 275 words'),
        ('2 pages / 550 words', '2 pages / 550 words'),
        ('3 pages / 825 words', '3 pages / 825 words'),
        ('4 pages / 1100 words', '4 pages / 1100 words'),
        ('5 pages / 1375 words', '5 pages / 1375 words'),
        ('6 pages / 1650 words', '6 pages / 1650 words'),
        ('7 pages / 1925 words', '7 pages / 1925 words'),
        ('9 pages / 2200 words', '9 pages / 2200 words'),
        ('10 pages / 2750 words', '10 pages / 2750 words'),
        ('11 pages / 3025 words', '11 pages / 3025 words'),
        ('12 pages / 3300 words', '12 pages / 3300 words'),
        ('13 pages / 3575 words', '13 pages / 3575 words'),
        ('14 pages / 3850 words', '14 pages / 3850 words'),
        ('15 pages/ 4125 words', '15 pages/ 4125 words'),
        ('16 pages / 4400 words', '16 pages / 4400 words'),
        ('17 pages / 4675  words', '17 pages / 4675  words'),
        ('18 pages / 4950 words', '18 pages / 4950 words'),
        ('19 pages / 5225 words', '19 pages / 5225 words'),
        ('20 pages / 5500 words', '20 pages / 5500 words'),
        ('21 pages / 5775 words', '21 pages / 5775 words'),
        ('22 pages / 6050 words', '22 pages / 6050 words'),
        ('23 pages / 6325 words', '23 pages / 6325 words'),
        ('24 pages / 6600  words', '24 pages / 6600  words'),
        ('25 pages / 6875 words', '25 pages / 6875 words'),
        ('26 pages / 7150 words', '26 pages / 7150 words'),
        ('27 pages / 7425 words', '27 pages / 7425   words'),
        ('28 pages / 7700 words', '28 pages / 7700 words'),
        ('29 pages / 7975 words', '29 pages / 7975 words'),
        ('30 pages / 8250  words', '30 pages / 8250  words'),
        
    


    )




    order_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250)
    description = models.TextField(validators=[MinLengthValidator(limit_value=10, message='Too short')])
    order_uuid = models.IntegerField(unique=True)
    order_type = models.CharField(max_length=250, choices=order_type, default='essay order')
    pages  = models.CharField(max_length=250, choices=page_choice, default='page choice')
    publication_date = models.DateField(default=timezone.now)
    service =  models.CharField(max_length=250, choices=service_choice, default='essay service')
    deadline = models.DateTimeField()
    sources = models.CharField(max_length=250, choices=source_choice, default='essay sources')
    completed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    style  = models.CharField(max_length=250, choices=style_choice, default='essay style')
    subject = models.CharField(max_length=250, choices=subject_choice, default='essay subject')
    level = models.CharField(max_length=250, choices=level_choice, default='essay level')
    bid_placed = models.BooleanField(default=False)
    

    class Meta:
        get_latest_by = 'publication_date'
        
    
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('customer:order_detail',  kwargs= {'order_uuid': self.order_uuid})

    def mail_writers(self, reciepent):
        context_object = {
            'order_uuid': self.order_uuid
        }
        return invite_writer(reciepent, **context_object)




class AdditionalFiles(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='additional_filesc')
    file_upload = models.FileField(upload_to='addition_files')

    
    
    def __str__(self):
        return str(self.user)



class FavouriteWriters(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_writer')
    favorite_writers = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_writers', null=True)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Hired(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hired')
    hired = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hired_before')

    def __str__(self):
        return str(self.user)


class Offers(models.Model):
    offer_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='offer_id')
    offers = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)







