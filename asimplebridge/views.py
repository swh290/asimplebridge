from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.models import User

def home(request):
  print request.user
  print request.user.is_authenticated()
  if request.user.is_authenticated():
    return HttpResponse("Hello, world. First Page!")
  else:
    return HttpResponse("Need Log In!")