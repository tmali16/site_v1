from datetime import timedelta

from django import template
from django.shortcuts import get_object_or_404
from django.utils import timezone

from Comment.models import Comment
from Posts.models import Post
from Service.models import Service

register = template.Library()


@register.filter
def comment_count(id):
    if Comment.objects.filter(object_id=id).count() > 0:
        res = Comment.objects.filter(object_id=id).count()
    else:
        res = '0'
    return res

@register.filter
def comment_post(id):
    res = []
    if Comment.objects.filter(object_id=id).count() > 0:
        comments = Comment.objects.filter(object_id=id).all()
        res.append(Post.objects.get(id=id).name)
        print(res)
    return res


@register.filter
def filter_comment(id):
    comments = Comment.objects.filter(object_id=id).all() #.filter(timestamp__range=(timezone.now(), timezone.now() - timedelta(hours=1)))
    r = []
    for s in comments:
        r.append(s.content)
        if len(r) > 2:
            break
    print('=> '+str(id))
    return r


@register.filter
def count_day(td):
    res = td - timezone.now()
    e_date = (timezone.now() + res) - timezone.now()
    day = e_date.days
    hours = e_date.seconds // 3600
    minute = (e_date.seconds // 60) % 60
    days_call = ''
    time_call = ''
    if day > 0:
        if 1 == day >= 4:
            days_call = 'день'
        elif 2 <= day <= 4:
            days_call = 'дня'
        return '{0} {1}'.format(day, days_call)
    elif hours > 0:
        if 1 == hours or hours == 21:
            time_call = 'час'
        elif 2 <= hours <= 4 or hours >= 22:
            time_call = 'часа'
        elif 5 <= hours <= 20:
            time_call = 'часов'
        return '{0} {1}'.format(hours, time_call)
    else:
        return '{0} ч. {1} минуты'.format(hours, minute)
