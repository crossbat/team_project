from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Notification, News


def event(request):
	noti_page = request.GET.get('event', '1')
	noti_list = Notification.objects.all().order_by('-create_date')
	noti_paginator = Paginator(noti_list, 20)
	noti_obj = noti_paginator.get_page(noti_page)
	context = {"noti_list" : noti_obj}
	
	return render(request, "event.html", context)

def news(request):
	news_page = request.GET.get('news', '1')
	news_list = News.objects.all().order_by('-create_date')
	news_paginator = Paginator(news_list, 20)
	news_obj = news_paginator.get_page(news_page)
	context = {"news_list" : news_obj}

	return render(request, "news.html", context)

