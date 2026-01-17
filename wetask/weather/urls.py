from django.urls import include, path

from .views import hello_weather

urlpatterns = [
    path("", hello_weather, name="weather"),
]
