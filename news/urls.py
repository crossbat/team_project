from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "news"

urlpatterns = [
		path("", views.news, name = "news"),
		path("/<int:news_id>/", views.detail),
]
