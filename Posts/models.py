import sys
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

# Create your models here.
from django.urls import reverse
from io import BytesIO

from image_cropping import ImageRatioField, ImageCropField
from sorl.thumbnail import get_thumbnail

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


class post_status(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=12, null=False)
    age = models.CharField(max_length=10)
    boob = models.FloatField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    note = models.TextField(max_length=1000, null=True, blank=True)
    hair = models.ForeignKey(haire, on_delete=models.CASCADE)
    eye = models.ForeignKey(eyes, on_delete=models.CASCADE)
    types = models.ForeignKey(types, on_delete=models.CASCADE)
    image_1 = ImageCropField(upload_to=file_location, blank=True, null=True)
    image_2 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_3 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_4 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_5 = models.ImageField(upload_to=file_location, blank=True, null=True)
    image_1_cropping = ImageRatioField('image_1', '1000x1000')
    image_2_cropping = ImageRatioField('image_2', '1000x1000')
    image_3_cropping = ImageRatioField('image_3', '1000x1000')
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    appart_1 = models.CharField(max_length=10, default="-", blank=True)
    appart_2 = models.CharField(max_length=10, default="-", blank=True)
    appart_naigth = models.CharField(max_length=10, default="-", blank=True)
    outside_1 = models.CharField(max_length=10, default="-", blank=True)
    outside_2 = models.CharField(max_length=10, default="-", blank=True)
    outside_nigth = models.CharField(max_length=10, default="-", blank=True)
    sauna_1 = models.CharField(max_length=10, default="-", blank=True)
    sauna_2 = models.CharField(max_length=10, default="-", blank=True)
    sauna_night = models.CharField(max_length=10, default="-", blank=True)

    active_counter = models.IntegerField(blank=True, null=True, default=0)
    user_active = models.BooleanField(default=True)
    end_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    admin_active = models.BooleanField(default=False)
    status = models.ForeignKey(post_status, on_delete=models.CASCADE, null=True, blank=True)
    engleash = models.BooleanField(default=False)

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

    # def save(self):
    #     img1 = Image.open(self.image_1)
    #     output = BytesIO()
    #     img1 = img1.resize((img1.size[0]//2, img1.size[1]//2), Image.NORMAL)
    #     img1.save(output, format="JPEG", quality=100)
    #     output.seek(0)
    #     self.image_1 = InMemoryUploadedFile(output, 'ImageField', "%s.jpeg" % self.image_1.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
    #
    #     super(Post, self).save()
