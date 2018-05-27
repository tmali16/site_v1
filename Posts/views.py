from django.core.paginator import *
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from datetime import *

from Comment.commentsForm import CommentForm
from Comment.models import Comment
from Service.models import Service
from Service.serviceForm import ServiceForm
from .activate import *
import time
import threading
# Create your views here.
from Posts.forms import *
from Posts.accauntForm import *
from Posts.models import Post


def post_list(request):
    title = "Главная"
    post = Post.objects.all()
    comment = Post.comments
    paginator = Paginator(post, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # title = "Войти"
    # count_to_end_active()
    checks()
    context = {
        "title": title,
        'post': post,
        'posts_page': posts,
        "comments": comment,
    }
    return render(request, "post_list.html", context)


def post_create(request):
    title = 'Новая анкета'
    form = pForm(request.POST or None, request.FILES or None)
    sform = ServiceForm(request.POST or None)
    if form.is_valid() and sform.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        service = sform.save(commit=False)
        service.post = post
        service.save()
        redirect('Posts:profile')
    context = {
        'title': title,
        'form': form,
        'sform': sform
    }
    return render(request, "post_form.html", context)


def post_update(request, id=None):
    title = 'Изменения'
    instance = get_object_or_404(Post, id=id)
    serv_instance = get_object_or_404(Service, post_id=id)
    form = pForm(request.POST or None, request.FILES or None, instance=instance)
    sform = ServiceForm(request.POST or None, instance=serv_instance)
    if form.is_valid() and sform.is_valid():
        mInstance = form.save(commit=False)
        mInstance.user = request.user
        mInstance.save()
        ins = sform.save(commit=False)
        ins.post = mInstance
        ins.save()
    context = {
        'title': title,
        'form': form,
        'sform': sform,
        'instance': instance
    }
    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    serviceInstance = get_object_or_404(Service, post_id=id)
    if not (instance.user_active and instance.admin_active):
        print("Not activate")
        raise Http404
    # if request.user.id != instance.user_id:
    #     raise Http404

    comment = Comment.objects.filter_by_instance(instance)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get("content")
        # parent_id = request.POST.get("parent_id")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments = instance.comments
    context = {
        "instance": instance,
        'serv_instance': serviceInstance,
        "comments": comments,
        "comment_form": comment_form,
    }
    return render(request, "test.html", context)


# ------------------------------------------------------------------------------------

def active_state(request, id):
    inst = get_object_or_404(Post, id=id)
    if inst.user_active:
        Post.objects.filter(id=id).update(user_active=False)
        redirect('Posts:profile')
    else:
        Post.objects.filter(id=id).update(user_active=True)
        redirect('Posts:profile')
    return redirect('Posts:profile')


def filter_excpencive(request):
    title = 'Главная'
    instance = Service.objects.all().select_related('post').order_by('appart_1')
    post = Post.objects.all()
    # title = "Войти"
    context = {
        "title": title,
        'post': instance,
    }
    return render(request, "post_list.html", context)


def yunger(request):
    title = 'Главная'
    post = Post.objects.all().order_by('age')
    # title = "Войти"
    context = {
        "title": title,
        'post': post,
    }
    return render(request, "post_list.html", context)


def new(request):
    title = 'Главная'
    post = Post.objects.all().order_by('timestamp')
    # title = "Войти"
    context = {
        "title": title,
        'post': post,
    }
    return render(request, "post_list.html", context)


def big_boobs(request):
    title = 'Главная'
    post = Post.objects.all().filter(boob__gt=3).order_by('boob')
    # title = "Войти"
    context = {
        "title": title,
        'post': post,
    }
    return render(request, "post_list.html", context)
