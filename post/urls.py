from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "Post"

urlpatterns = [
	path("", views.post, name = "post"),
    path("/<int:post_id>/", views.detail),
]
