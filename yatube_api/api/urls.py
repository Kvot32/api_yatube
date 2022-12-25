from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentsViewSet, GroupViewSet, PostViewSet

app_name = "api"

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(r"posts/(?P<post_id>\d+)/comments", CommentsViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
