from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from bot import Bot
import aiml

k = aiml.Kernel()
k.learn('std-startup.xml')
k.respond('load aiml b')

def landing(request):
    return render_to_response('base.html', context=RequestContext(request))

def chat(message):
    b = Bot()
    a = b.connect()
    rep = b.message(a, message)
    return HttpResponse(rep)
