from django.shortcuts import get_object_or_404
from django.utils import timezone
from Posts.models import Post
from datetime import timedelta
import time
import threading


def checks():
    # def autoDeActive(self):
        if Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True):

            for id in Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True).order_by('id'):
                a_active = get_object_or_404(Post, id=id).admin_active
                u_active = get_object_or_404(Post, id=id).user_active
                e_date = get_object_or_404(Post, id=id).end_date
                s_date = get_object_or_404(Post, id=id).start_date
                if a_active and u_active:
                    if timezone.now() > e_date:
                        Post.objects.filter(id=id).update(admin_active=False)
                        print('deActivated')
                    else:
                        Post.objects.filter(id=id).update(start_date=timezone.now())
                        print('Anketa #'+str(id)+' works')
                else:
                    if not u_active and a_active:
                        res_date = timezone.now() - e_date

def count_to_end_active(active_date, id):
    today = timezone.now()
    active_to_date = timedelta(days=active_date)
    end_date = get_object_or_404(Post, id=id).end_date
    while True:
        if timezone.now() > end_date:
            Post.objects.filter(id=id).update(admin_active=False)
            print('deActivated')
            break
        else:
            return (timezone.now()-end_date)
            time.sleep(86400)