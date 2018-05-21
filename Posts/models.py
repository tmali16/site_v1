from django.contrib.auth.models import User
from django.db import models


# Create your models here.
def file_location(instance, filename):
    return "form_%s/%s" % (instance.id, filename)


class eyes(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class body(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class types(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class haire(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class active_days(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, null=False)
    age = models.CharField(max_length=10)
    boob = models.CharField(max_length=5)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=5)
    note = models.TextField(max_length=500)
    hair = models.ForeignKey(haire, on_delete=models.CASCADE)
    eye = models.ForeignKey(eyes, on_delete=models.CASCADE)
    types = models.ForeignKey(types, on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_2 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_3 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_4 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_5 = models.ImageField(upload_to=file_location, blank=True, null=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    user_active = models.BooleanField(default=True)
    active_day = models.ForeignKey(active_days, on_delete=models.CASCADE)
    end_date = models.DateTimeField(auto_now_add=False, null=True)
    admin_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    appart_1 = models.CharField(max_length=10, default="-", blank=True)
    appart_2 = models.CharField(max_length=10, default="-", blank=True)
    appart_naigth = models.CharField(max_length=10, default="-", blank=True)
    outside_1 = models.CharField(max_length=10, default="-", blank=True)
    outside_2 = models.CharField(max_length=10, default="-", blank=True)
    outside_nigth = models.CharField(max_length=10, default="-", blank=True)

    main_classic = models.BooleanField(default=False)
    main_blowJob_w_condom = models.BooleanField(default=False)
    main_cunni = models.BooleanField(default=False)
    main_group_sex = models.BooleanField(default=False)
    main_lesbi_lesbi = models.BooleanField(default=False)

    mbr = models.BooleanField(default=False)
    mbr_price = models.TextField(max_length=10, null=True, blank=True)
    anal_sex = models.BooleanField(default=False)
    anal_sex_price = models.TextField(max_length=10, null=True, blank=True)

    dop_end_mouth = models.BooleanField(default=False)
    dop_end_face = models.BooleanField(default=False)
    dop_glub_minet = models.BooleanField(default=False)
    dop_toys = models.BooleanField(default=False)
    dop_role_game = models.BooleanField(default=False)
    dop_couple_service = models.BooleanField(default=False)
    dop_video = models.BooleanField(default=False)
    dop_company = models.BooleanField(default=False)

    massage_relax = models.BooleanField(default=False)
    massage_classic = models.BooleanField(default=False)
    massage_profi = models.BooleanField(default=False)
    massage_tiski = models.BooleanField(default=False)
    massage_prostat = models.BooleanField(default=False)
    massage_erotic = models.BooleanField(default=False)
    massage_sakura = models.BooleanField(default=False)

    dance_profi = models.BooleanField(default=False)
    dance_NoProfi = models.BooleanField(default=False)
    dance_lesbi_show = models.BooleanField(default=False)
    dance_lisbi = models.BooleanField(default=False)

    sado_bandaj = models.BooleanField(default=False)
    sado_gospoja = models.BooleanField(default=False)
    sado_rabyn = models.BooleanField(default=False)
    sado_dominant = models.BooleanField(default=False)
    sado_porka = models.BooleanField(default=False)
    sado_fetish = models.BooleanField(default=False)
    sado_trampling = models.BooleanField(default=False)

    extrim_anilingus = models.BooleanField(default=False)
    extrim_dojd_out = models.BooleanField(default=False)
    extrim_dojd_in = models.BooleanField(default=False)
    extrim_strapon = models.BooleanField(default=False)
    extrim_fisting_anal = models.BooleanField(default=False)
    extrim_fisting_vagin = models.BooleanField(default=False)

    def __str__(self):
        return self.post
