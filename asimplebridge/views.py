import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from account.models import *
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
  if request.user.is_authenticated():
    userName = request.user
    if request.user.is_staff:
      return render(request, 'homepage.html', locals())
    picture = get_picture(request.user)
    gender = get_gender(request.user)
    location = get_location(request.user)
    friends = []
    friendNum = len(friends)
    return render(request, 'lobby.html', locals())
  else:
    return render(request, 'login.html', locals())

@csrf_exempt
def login(request):
  if request.POST:
    user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
      if user.is_active:
        userName = request.user
        auth.login(request, user)
  return HttpResponseRedirect("/")

def signup(request):
  return render(request, 'signup.html', locals())

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

@csrf_exempt
def register(request):
  if request.POST:
    userName = request.POST.get('username')
    password =request.POST.get('password')
    email = request.POST.get('email')
    if not User.objects.filter(username=userName).exists() and not User.objects.filter(email=email).exists():
      user = User.objects.create(username=userName, email=email)
      user.set_password(password)
      user.save()
      return render(request, 'login.html', locals())
  return HttpResponseRedirect("/signup")
