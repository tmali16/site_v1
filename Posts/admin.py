from django.contrib import admin

# Register your models here.
from Posts.models import *
from Service.models import Service

admin.site.register(Post)
admin.site.register(haire)
admin.site.register(eyes)
admin.site.register(types)
admin.site.register(post_status)

admin.site.register(Service)
admin.site.register(Comment)
