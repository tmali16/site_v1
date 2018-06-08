from django.shortcuts import get_object_or_404
from django.utils import timezone
from Posts.models import Post
from datetime import timedelta


def count_end_date(d, c):
    if d >= c:
        count = (d - (d - c))
        if (d - count) >= 0:
            day = timezone.now() + timedelta(hours=count)
            return day
        else:
            return timezone.now()
    else:
        return timezone.now()


def active_object(id, day_to_active):
    inst = get_object_or_404(Post, id=id)
    if inst.user_active and inst.admin_active:
        if inst.active_counter > 0 or inst.active_counter is not None and not inst.admin_active:
            return 2
        else:
            return 3
    else:
        if inst.end_date is None:
            d = count_end_date(inst.active_counter, day_to_active)
            if d > timezone.now():
                Post.objects.filter(id=id).update(end_date=d)
                Post.objects.filter(id=id).update(active_counter=(inst.active_counter - u_name))
                Post.objects.filter(id=id).update(user_active=True)
                Post.objects.filter(id=id).update(admin_active=True)
                return 1
            else:
                return 0
        elif (timezone.now() > inst.end_date) and inst.active_counter > 0:
            d = count_end_date(inst.active_counter, day_to_active)
            if d > timezone.now():
                Post.objects.filter(id=id).update(end_date=d)
                Post.objects.filter(id=id).update(active_counter=(inst.active_counter - u_name))
                Post.objects.filter(id=id).update(user_active=True)
                Post.objects.filter(id=id).update(admin_active=True)
                return 1
            else:
                return 0
        else:
            Post.objects.filter(id=id).update(user_active=True)
            Post.objects.filter(id=id).update(admin_active=True)
            return 2


def checks():
    for i in Post.objects.values_list('id', flat=True).filter(user_active=True).filter(admin_active=True).order_by(
            'id'):
        toDay = timezone.now()
        activ_days = get_object_or_404(Post, id=i).active_counter
        e_date = get_object_or_404(Post, id=i).end_date

        if toDay > e_date:
            if 0 < activ_days:
                Post.objects.filter(id=i).update(user_active=False)
            else:
                Post.objects.filter(id=i).update(admin_active=False)
        else:
            print('Анкета №{0} активна'.format(id))


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
                end = (timezone.now() - end_date)
                # Post.objects.filter(id=id).update(active_day=end.minute)
                print(end)
