from django.contrib.auth import login as auth_login, authenticate, logout
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils import timezone

from Posts.accauntForm import *
from Posts.models import Post


def login(request):
    title = "Войти"
    btnTitle = 'Войти'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return redirect("Posts:profile")
    return render(request, "accaunt_form.html", {"authForm": form, "title": title, 'btn' : btnTitle})


def register_view(request):
    title = "Регистрация"
    btnTitle = 'Регистрация'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        # user_gains_perms(request, user_id=user.id)
        new_user = authenticate(username=user.username, password=password)
        auth_login(request, new_user)
        return redirect("Posts:profile")
    context = {
        'authForm': form,
        'title': title,
        'btn' : btnTitle

    }
    return render(request, "accaunt_form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/post")


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
