from django import template
from django.shortcuts import get_object_or_404
from django.utils import timezone

from Posts.models import Post
from Service.models import Service

register = template.Library()

@register.filter
def appart_1(id):
    res = get_object_or_404(Service, post_id=id)
    return res.appart_1

@register.filter
def appart_2(id):
    print('apprt_2 {0}'.format(id))
    res = get_object_or_404(Service, post_id=id)
    return res.appart_2
@register.filter
def appart_night(id):
    print('appart_night {0}'.format(id))
    res = get_object_or_404(Service, post_id=id)
    return res.appart_naigth
@register.filter
def outside_1(id):
    res = get_object_or_404(Service, post_id=id)
    return res.outside_1
@register.filter
def outside_2(id):
    res = get_object_or_404(Service, post_id=id)
    return res.outside_2
@register.filter
def outside_night(id):
    res = get_object_or_404(Service, post_id=id)
    return res.outside_nigth

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