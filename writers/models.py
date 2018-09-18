from django.db import models
from django.conf import settings
from customer.models import Order

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class WritersProfile(models.Model):
    profile_id = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',
    on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    headline = models.CharField(max_length=30)
    about = models.TextField()

    def __str__(self):
        return str(self.profile_id)


class Rating(models.Model):
    rating_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rating')
    reviews = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    num_of_orders_completed = models.IntegerField(default=0)

    def __str__(self):
        return str(self.reviews)


    
class Bids(models.Model):
    bidding_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='bid_order', null=True)
    bidders = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bidders',null=True)
    declined = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    shortlisted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bidding_id)



