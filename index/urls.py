from django.urls import path, include
from . import views

app_name = "index"

urlpatterns = [
		path('', views.index, name = "index"),
		path('intro', views.intro, name = 'intro'),
		path('mission', views.mission, name = 'mission'),
		path('member', views.member, name = 'member'),
]
