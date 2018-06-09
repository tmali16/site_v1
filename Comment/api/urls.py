from django.conf.urls import url

from Comment.api.views import (
    CommentListAPIView
)

app_name = "Comment-api"

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name="list"),
    # url(r'^(?P<pk>\d+)/$', DetaileViewAPI.as_view(), name="edite"),
    # url(r'^(?P<id>\d+)/active/$', views.active_state, name="active_state"),
]