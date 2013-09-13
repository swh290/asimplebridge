from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField( User, unique=True)

  fbId = models.BigIntegerField( default = 0 )
  fbAccessToken = models.CharField( max_length = 255, blank=True, null=True )
  first_name = models.CharField( max_length = 50)
  last_name = models.CharField( max_length = 50)
  username = models.CharField( max_length = 50)

admin.site.register(UserProfile)

def create_userProfile(user, fbId, fbAccessToken, first_name, last_name, username):
  userProfile = UserProfile.objects.create(user=user, fbId=fbId, fbAccessToken=fbAccessToken, first_name=first_name,last_name=last_name, username=username)
  userProfile.save()