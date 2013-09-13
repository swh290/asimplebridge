import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from django.contrib.auth.models import User
from account.models import *

@csrf_exempt
def fbRegister(request):
  response_data = {}
  response_data['success'] = 'false'
  print request.method
  if request.method == 'POST':
    fbAccessToken = request.POST.get('fbAccessToken')
    fbId = request.POST.get('fbID')
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    user = User.objects.create(username=username)
    user.set_password("123456")
    user.save()
    create_userProfile(user, fbId, fbAccessToken, first_name, last_name, username)
    response_data['success'] = 'true'

  return HttpResponse( json.dumps(response_data))
