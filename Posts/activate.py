from django.shortcuts import get_object_or_404
from django.utils import timezone
from Posts.models import Post
import threading


def checks():
    # def autoDeActive(self):
        if Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True):

            for id in Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True).order_by('id'):
                a_active = get_object_or_404(Post, id=id).admin_active
                u_active = get_object_or_404(Post, id=id).user_active
                e_date = get_object_or_404(Post, id=id).end_date
                if a_active and u_active:
                    if timezone.now() > e_date:
                        Post.objects.filter(id=id).update(admin_active=False)
                        print('deActivated')
                    else:
                        Post.objects.filter(id=id).update(start_date=timezone.now())
                        print('Anketa #'+str(id)+' works')

                    # Post.objects.values('id', 'user_active', 'admin_active', 'start_date', 'end_date').filter(
                    # user_active=True).filter(admin_active=True):
