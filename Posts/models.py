from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
from django.urls import reverse

from Comment.models import Comment


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


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, null=False)
    age = models.CharField(max_length=10)
    boob = models.FloatField(max_length=5)
    height = models.IntegerField(max_length=5)
    weight = models.IntegerField(max_length=5)
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
    end_date = models.DateTimeField(auto_now_add=False, null=True)
    admin_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Posts:detail", kwargs={"id": self.id})

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs



    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type