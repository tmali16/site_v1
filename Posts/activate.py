from django.shortcuts import get_object_or_404
from django.utils import timezone
from Posts.models import Post
from datetime import timedelta
import time
import threading


def checks():
    for i in Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True).order_by('id'):
        toDay = timezone.now()
        a_active = get_object_or_404(Post, id=i).admin_active
        u_active = get_object_or_404(Post, id=i).user_active
        # e_date = get_object_or_404(Post, id=i).end_date
        if a_active and u_active:
            Post.objects.filter(id=i).update(active_counter=None)
        else:
            pass


def count_to_end_active():
    for id in Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True).order_by(
            'id'):
        a_active = get_object_or_404(Post, id=id).admin_active
        u_active = get_object_or_404(Post, id=id).user_active
        if a_active and u_active:
            end_date = get_object_or_404(Post, id=id).end_date
            if timezone.now() > end_date:
                Post.objects.filter(id=id).update(admin_active=False)
                print('deActivated')
            else:
                end = (timezone.now()-end_date)
                # Post.objects.filter(id=id).update(active_day=end.minute)
                print(end)
