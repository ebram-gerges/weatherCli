import requests
from django.shortcuts import render


# Create your views here.
def hello_weather(request):
    return render(request, "weather.html", {"message": "hello world!"})
