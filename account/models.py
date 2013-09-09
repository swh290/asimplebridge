from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class UserProfile(models.Model):
      user = models.OneToOneField( User, unique=True )

admin.site.register(UserProfile)
