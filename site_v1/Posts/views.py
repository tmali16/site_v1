from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
# Create your views here.
from Posts.forms import *
from Posts.accauntForm import *
from Posts.models import Post


def post_list(request):
    title = "Главная"
    post = Post.objects.all()
    # title = "Войти"
    forms = UserLoginForm(request.POST or None)
    if forms.is_valid():
        username = forms.cleaned_data.get("username")
        password = forms.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("posts:profile")
    context = {
        "title": title,
        'post': post,
        'authForm': forms,
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
    context = {
        "instance": instance,
        # "comments": comments,
        # "comment_form": comment_form,
    }
    return render(request, "detail.html", context)

# ------------------------------------------------------------------------------------
