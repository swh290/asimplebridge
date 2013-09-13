from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
  user = models.ForeignKey( User, unique=True)

  fbId = models.BigIntegerField( default = 0 )
  fbAccessToken = models.CharField( max_length = 255, blank=True, null=True )

admin.site.register(UserProfile)

def create_userProfile(user, fbId, fbAccessToken):
  userProfile = UserProfile.objects.create(user=user, fbId=fbId, fbAccessToken=fbAccessToken)
  userProfile.save()