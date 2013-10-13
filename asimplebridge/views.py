import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.contrib.auth.models import User
from account.models import *
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import redis

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
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('chat', userName)
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

@csrf_exempt
def node_api(request):
  try:
    #Get User from sessionid
    # session = Session.objects.get(session_key=request.POST.get('sessionid'))
    # user_id = session.get_decoded().get('_auth_user_id')
    # user = User.objects.get(id=user_id)

    #Create comment
    # Comments.objects.create(user=user, text=request.POST.get('comment'))
    
    #Once comment has been created post it to the chat channel
    if request.POST:
      data = request.POST
      data = data.get('comment')
      jsonRequest = json.loads(data)

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('chat', jsonRequest.get('author') + ": " + jsonRequest.get('message'))
    
    return HttpResponse("Everything worked :)")
  except Exception, e:
    return HttpResponseServerError(str(e))
