from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentsViewSet, GroupViewSet, PostViewSet

app_name = "api"

router_v1 = SimpleRouter()
router_v1.register("posts", PostViewSet)
router_v1.register("groups", GroupViewSet)
router_v1.register(r"posts/(?P<post_id>\d+)/comments",
                   CommentsViewSet,
                   basename='comment'
                   )


urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
