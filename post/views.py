from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator
from .models import Post

def post(request):
    post_page = request.GET.get('post', '1')
    post_list = Post.objects.all().order_by('-create_date')
    post_paginator = Paginator(post_page, 16)
    post_obj = post_paginator.get_page(post_page)
    context = {"post_list" : post_obj}

    return render(request, "post/post.html", context)

def detail(request, post_id):
    post = Post.objects.get(id = post_id)
    context = {'post' : post}
    return render(request, 'post/post_detail.html', context)

