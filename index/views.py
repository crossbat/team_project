from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from eventNews.models import Notification, News

def index(request):
	noti_list = Notification.objects.all().order_by('-create_date')[:3]

	news_list = News.objects.all().order_by('-create_date')[:3]
	context = {'noti_list' : noti_list, 'news_list' : news_list}
	
	return render(request, 'index.html', context)
