from django.contrib import messages
from django.core.paginator import *
from django.http import Http404, HttpResponseRedirect, HttpResponse
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
    post = Post.objects.all().order_by('-status')
    paginator = Paginator(post, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    comment = Comment.objects.filter(parent=1)
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
        'post': posts,
        'comment': comment
    }
    return render(request, "post_list.html", context)


def post_create(request):
    if not request.user.is_authenticated:
        raise Http404
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
        messages.success(request, 'Анкета создано!')
        redirect('/')
    context = {
        'title': title,
        'form': form,
        'sform': sform
    }
    return render(request, "post_form.html", context)


def post_update(request, id=None):
    if not request.user.is_authenticated:
        raise Http404
    title = 'Изменения'
    instance = get_object_or_404(Post, id=id)
    if request.user.id != instance.user_id:
        raise Http404
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
        messages.success(request, 'Изменение сохранены!')
    context = {
        'title': title,
        'form': form,
        'sform': sform,
        'instance': instance
    }
    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    return render(request, "post_form.html")


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    serviceInstance = get_object_or_404(Service, post_id=id)

    if not request.user.is_authenticated:
        if not (instance.user_active and instance.admin_active):
            print("Not activate")
            raise Http404
    if not instance.user_active or not instance.admin_active:
        if request.user.id != instance.user_id:
            print('its not you anket')
            raise Http404
    if request.user.is_authenticated:
        user = request.user
    else:
        user = get_object_or_404(User, id=2)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    # if request.user.is_authenticated:
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content_data = comment_form.cleaned_data.get("content")
        if request.user.is_authenticated:
            u_name = request.user.username
        else:
            u_name = comment_form.cleaned_data.get("username")
        parent_id = request.POST.get("parent_id")
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
            user=user,
            username=u_name,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj,
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
        # return redirect('Posts:detail', id=obj_id)
    else:
        pass
        # messages.warning(request, 'not valid comment')
    comments = instance.comments
    context = {
        "comments": comments,
        "comment_form": comment_form,
        "instance": instance,
        'serv_instance': serviceInstance
    }
    return render(request, "detail_post.html", context)


def test(request, id=None):
    if request.GET:
        u_name = request.GET['content']
        return HttpResponse('no', content_type='text/html')


# ------------------------------------------------------------------------------------
def one_day(d):
    return d - (d - 1)


def count_end_date(d):
    day = timezone.now() + timedelta(minutes=one_day(d))
    return day


def active_state(request, id):
    inst = get_object_or_404(Post, id=id)
    if inst.user_active:
        Post.objects.filter(id=id).update(user_active=False)
        redirect('Posts:profile')
    else:
        Post.objects.filter(id=id).update(user_active=True)
        redirect('Posts:profile')
    return redirect(inst.get_absolute_url())


def filter_excpencive(request):
    title = 'Главная'
    instance = Service.objects.all()
    post = Post.objects.all().filter(appart_1__gt=3000).order_by('-appart_1')
    # title = "Войти"
    context = {
        "title": title,
        'post': post,
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
