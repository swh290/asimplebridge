from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect
from django_socketio import events
import django_socketio

@events.on_message(channel="lobby")
def my_chat_handler(request, socket, context, message):
  django_socketio.broadcast_channel(message, 'lobby')
