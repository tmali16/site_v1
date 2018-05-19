from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from Posts.accaunt_view import *
from Posts import views
app_name = "Posts"
urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name="edit"),
]
