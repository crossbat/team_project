from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import News

def news(request):
	news_page = request.GET.get('news', '1')
	news_list = News.objects.all().order_by('-create_date')
	news_paginator = Paginator(news_list, 20)
	news_obj = news_paginator.get_page(news_page)
	context = {"news_list" : news_obj}

	return render(request, "news/news.html", context)

def detail(request, news_id):
	news = News.objects.get(id = news_id)
	context = {'news':news}
	return render(request, 'news/news_detail.html', context)
