from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
  user = models.ForeignKey( User, primary_key=True)

  fbId = models.BigIntegerField( default = 0 )
  fbAccessToken = models.CharField( max_length = 255, blank=True, null=True )
  picture = models.CharField( max_length = 255, blank=True, null=True )

  def __unicode__(self):
    return self.user.username

admin.site.register(UserProfile)

def create_userProfile(user, fbId = 1, fbAccessToken = "", picture = ""):
  userProfile = UserProfile.objects.create(user=user, fbId=fbId, fbAccessToken=fbAccessToken, picture=picture)
  userProfile.save()