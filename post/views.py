from django.shortcuts import render
from django.template import loader

def post(request):
	return render(request, "post/post.html")

