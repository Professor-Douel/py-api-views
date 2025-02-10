from django.urls import (
    path,
    include
)

from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("ctors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("halls/", hall_list, name="hall-list"),
    path("halls/<int:pk>/", hall_detail, name="hall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
