import requests
import sys

sys.path.append('pycharm-debug.egg')

import pydevd
import os
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

pydevd.settrace('locahost', port='9090', stdoutToServer=True, stderrToServer=True)

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES', 3))
    #r = requests.get('http://httpbin.org/status/418')
    #print r.text
    #return HttpResponse('<pre>' + r.text + '</pre>')
    return HttpResponse('New Code2')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

