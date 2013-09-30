import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from django.contrib.auth.models import User
from account.models import *

@csrf_exempt
def fbLogin(request):
  response_data = {}
  response_data['success'] = 'false'
  if request.method == 'POST':
    fbAccessToken = request.POST.get('fbAccessToken')
    fbId = request.POST.get('fbID')
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get('email')
    picture = request.POST.get('picture')
    location = request.POST.get('location')
    gender = request.POST.get('gender')
    # need to generate hash password
    password = '123456'

    user = UserProfile.objects.filter(fbId = fbId)
    if len(user) == 0:
      user = fbRegister(user, fbId, fbAccessToken, username, password, first_name, last_name, email, picture, location, gender)
    else:
      loginUser = auth.authenticate(username=username, password=password)
      if loginUser is not None:
        if loginUser.is_active:
          auth.login(request, loginUser)

      response_data['success'] = 'true'

  return HttpResponse( json.dumps(response_data))

def fbRegister(user, fbId, fbAccessToken, username, password, first_name, last_name, email, picture, location, gender):
  user = User.objects.create(username=username)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email
  
  user.set_password(password)
  user.save()
  create_userProfile(user, fbId, fbAccessToken, picture, location, gender)
  return user
