from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.models import User

def home(request):
  if request.user.is_authenticated():
    userName = request.user
    return render(request, 'homepage.html', locals())
  else:
    return render(request, 'login.html', locals())