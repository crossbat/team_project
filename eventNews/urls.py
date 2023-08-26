from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "eventNews"

urlpatterns = [
		path("event", views.event, name = "event"),
		path("news", views.news, name = "news")
]
