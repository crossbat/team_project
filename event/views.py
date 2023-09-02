from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from .models import Notification

def event(request):
	noti_page = request.GET.get('event', '1')
	noti_list = Notification.objects.all().order_by('-create_date')
	noti_paginator = Paginator(noti_list, 20)
	noti_obj = noti_paginator.get_page(noti_page)
	context = {"noti_list" : noti_obj}
	
	return render(request, "event/event.html", context)

def detail(request, noti_id):
	noti = Notification.objects.get(id = noti_id)
	context = {'noti':noti}
	return render(request, 'event/noti_detail.html', context)
