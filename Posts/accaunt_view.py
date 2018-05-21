from django.contrib.auth import authenticate, logout
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils import timezone

from Posts.accauntForm import *
from Posts.models import Post
from .views import active_state

def login(request):
    title = "Войти"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("Posts:profile")
    return render(request, "modal.html", {"authForm": form, "title": title})

def log_in(request):
    if request.GET:
        log = request.GET['username']
        # pass_ = request.POST['password']
        # user = authenticate(username=log, password=pass_)
        # login(request, user)
        # return redirect('Post:profile')
        print('hi')

def register_view(request):
    title = "Регистрация"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        # user_gains_perms(request, user_id=user.id)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/posts/profile")
    context = {
        'form': form,
        'title': title

    }
    return render(request, "accaunt_form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/posts")


def profile_view(request):
    if not request.user.is_authenticated:
        raise Http404
    active_day = timezone.now()
    title = "Мой профиль"
    user = request.user
    data_list = Post.objects.all().filter(user=user.id)
    context = {
        'user': user,
        'title': title,
        'posts': data_list,
        'tizone': active_day
    }
    return render(request, "profile.html", context)