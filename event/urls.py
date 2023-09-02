from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "event"

urlpatterns = [
		path("", views.event, name = "event"),
		path('/<int:noti_id>/', views.detail),
]
