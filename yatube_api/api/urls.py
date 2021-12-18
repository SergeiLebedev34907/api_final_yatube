# api/urls.py
from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowList, GroupViewSet, PostViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowList.as_view()),
]
