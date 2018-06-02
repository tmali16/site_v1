from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from Posts.accaunt_view import *
from Posts import views

app_name = "Posts"
urlpatterns = [
    url(r'^$', views.post_list, name="list"),

    url(r'^create/$', views.post_create, name="create"),
    # url(r'^create_serv/$', views.post_create_, name="create_"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', register_view, name="register"),
    url(r'^profile/$', profile_view, name="profile"),
    url(r'^(?P<id>\d+)/active/$', views.active_state, name="active_state"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name="edit"),
    url(r'^(?P<id>\d+)/edit_profile/$', profile_update, name="prof_ed"),

    # -----------------------ajax--------------------------------
    url(r'^(?P<id>\d+)/$', views.test, name="test"),

    # ---------------------filter-------------------------------

    url(r'^filter_1/$', views.filter_excpencive, name="expencive"),
    url(r'^filter_2/$', views.yunger, name="yunger"),
    url(r'^filter_3/$', views.new, name="new"),
    url(r'^filter_4/$', views.big_boobs, name="boobs"),
]