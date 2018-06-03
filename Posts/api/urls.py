from django.conf.urls import url

from Posts.api.views import (
    DetaileViewAPI,
    PostListAPIView
)

app_name = "Posts-api"

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', DetaileViewAPI.as_view(), name="edite"),
    # url(r'^(?P<id>\d+)/active/$', views.active_state, name="active_state"),
]
