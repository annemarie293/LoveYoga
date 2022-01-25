from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(modesl.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=False, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country *", null=True, blank=True)

    def __str__(self):
        return self.user.username



@reciver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Each time a user object is saved, a new user profile is created, or existing profile is updated
    """

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
