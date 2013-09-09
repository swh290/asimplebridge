from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
  if request.user.is_authenticated():
    userName = request.user
    return render(request, 'homepage.html', locals())
  else:
    return render(request, 'login.html', locals())

def login(request):
  if request.POST:
    user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
      if user.is_active:
        userName = request.user
        auth.login(request, user)
        return HttpResponseRedirect("/")
  return render(request, 'login.html', locals())

def signup(request):
  return render(request, 'signup.html', locals())

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect("/")

def register(request):
  if request.POST:
    userName = request.POST.get('username')
    password =request.POST.get('password')
    user = User.objects.create(username=userName)
    user.set_password(password)
    user.save()
    print 'save'
    return render(request, 'login.html', locals())
  print 'fail'
  return HttpResponseRedirect("signup")
