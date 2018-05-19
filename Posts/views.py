from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import *
from .activate import checks
import time
import threading
# Create your views here.
from Posts.forms import *
from Posts.accauntForm import *
from Posts.models import Post


def post_list(request):
    title = "Главная"
    post = Post.objects.all()
    # title = "Войти"
    threading.Timer(1.0, checks).start()
    context = {
        "title": title,
        'post': post,
    }
    return render(request, "post_list.html", context)


def post_create(request):
    title = 'Новая анкета'
    form = pForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        ins = form.save(commit=False)
        ins.save()
    context = {
        'title': title,
        'form': form
    }
    return render(request, "post_form.html", context)


def post_update(request, id=None):
    title = 'Изменения'
    instance = get_object_or_404(Post, id=id)
    form = pForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        ins = form.save(commit=False)
        ins.save()
    context = {
        'title': title,
        'form': form,
        'instance': instance
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated:
        if not (instance.user_active and instance.admin_active):
            print("Not activate")
            raise Http404
    else:
        if request.user.id != instance.user_id:
            raise Http404
    context = {
        "instance": instance,
        # "comments": comments,
        # "comment_form": comment_form,
    }
    return render(request, "detail.html", context)
# ------------------------------------------------------------------------------------



