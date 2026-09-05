from django.urls import path

from . import views

app_name = "comics"

urlpatterns = [
    path("", views.home, name="home"),
    path("comic/<slug:slug>/", views.reader, name="reader"),
    path("settings/", views.preferences, name="preferences"),
]
