from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
  GENDER_CHOICES = (('male', 'male'), ('female', 'female'), ('unknow', 'unknow'))

  user = models.ForeignKey( User, primary_key=True)

  fbId = models.BigIntegerField( default = 0 )
  fbAccessToken = models.CharField( max_length = 255, blank=True, null=True )
  picture = models.CharField( max_length = 255, blank=True, null=True )
  location = models.CharField( max_length = 255, blank=True, null=True )
  gender = models.CharField( choices=GENDER_CHOICES, max_length = 10, blank=True, null=True, default="unknow" )

  def __unicode__(self):
    return self.user.username

admin.site.register(UserProfile)

def create_userProfile(user, fbId = 1, fbAccessToken = "", picture = "", location = "", gender = "unknow"):
  userProfile = UserProfile.objects.create(user=user, fbId=fbId, fbAccessToken=fbAccessToken, picture=picture, location=location, gender=gender)
  userProfile.save()

def get_picture(user):
  profile = UserProfile.objects.get(user=user)
  return profile.picture

def get_gender(user):
  profile = UserProfile.objects.get(user=user)
  return profile.gender

def get_location(user):
  profile = UserProfile.objects.get(user=user)
  return profile.location
