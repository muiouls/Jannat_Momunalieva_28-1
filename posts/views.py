from django.shortcuts import HttpResponse
from datetime import datetime

# Create your views here.
""" MVC - Model View Controller """

""" Controller's """


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date_view(request):
    if request.method == 'GET':
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse("Date: " + now)


def goodby_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")
