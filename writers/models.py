import uuid
import random
from decimal import Decimal

from django.db import models

from django.db.models import F
from django.conf import settings
from customer.models import Order

from multiselectfield import MultiSelectField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class WritersProfile(models.Model):
    
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
    profile_id = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',
    on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image')
    full_name = models.CharField(max_length=50, null=True)
    headline = models.CharField(max_length=30)
    about = models.TextField()
    is_approved = models.BooleanField(default=False)
    profile_set = models.BooleanField(default=False)

    paypal_id = models.CharField(max_length=50)
    is_writer = models.BooleanField(default=False)
    subject = MultiSelectField(choices=subject_choice, max_choices=3)

    def __str__(self):
        return str(self.profile_id)


class Rating(models.Model):
    rating_id =  models.ForeignKey(WritersProfile, on_delete=models.CASCADE, related_name='reviews', null=True)
    review = models.CharField(max_length=250)
    rating = models.IntegerField()



    
class InvitedWriters(models.Model):
    user = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invited_writers')
    invitees = models.ForeignKey(WritersProfile, on_delete=models.CASCADE, related_name='invitees')
    invited = models.BooleanField(default=False)
    

    
class Bids(models.Model):
    id  = models.AutoField(max_length=7, primary_key=True)
    bidding_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='bid_order', null=True)
    bidders = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bidders',null=True)
    declined = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    in_progress = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    shortlisted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2, max_digits=20, default=Decimal('0.00'))


    def generated_unique_id(self):
        ran = ''.join(str(random.randint(2, 8)) for x in range(6))
        return ran

 
    def save(self, **kwargs):
        from customer.models import Offers
        self.id = self.generated_unique_id()
        offer = Offers.objects.get(offer_id=self.bidding_id)
        if offer.offers == 1:
            return super().save(**kwargs)
        else:
            Offers.objects.filter(offer_id=self.bidding_id).update(offers=F('offers')+ 1)
            return super().save(**kwargs)

    def __str__(self):
        return str(self.pk)


class AssignmentFiles(models.Model):
    id  = models.AutoField(max_length=7, primary_key=True)
    file_id = models.ForeignKey(Bids, on_delete=models.CASCADE)
    download_file = models.FileField(upload_to='download_assignment')
    description = models.CharField(max_length=15, null=True)



    def generated_unique_id(self):
        ran = ''.join(str(random.randint(2, 8)) for x in range(6))
        return ran

    def save(self, **kwargs):
        self.id = self.generated_unique_id()
        super().save(**kwargs)

    def __str__(self):
        return str(self.id)



