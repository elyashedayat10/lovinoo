from django.urls import path

from .views import (AddTOFavoriteApiView, BlockCreateApiView, BlockListApiView,
                    BlockRemoveApiView, FavoriteListApiView,
                    RemoveFromFavoriteApiView, ReportCreateApiView,
                    ReportListApiView)

urlpatterns = [
    path("reported_list/", ReportListApiView.as_view()),
    path("reporte_create/", ReportCreateApiView.as_view()),
    path("blocked_list/", BlockListApiView.as_view()),
    path("block_create/", BlockCreateApiView.as_view()),
    path("favorite_list/", FavoriteListApiView.as_view()),
    path("block_remove/", BlockRemoveApiView.as_view()),
    path("favorite_remove/", RemoveFromFavoriteApiView.as_view()),
    path("favorite_add/", AddTOFavoriteApiView.as_view()),
    # path("<int:pk>/", BlockRetravie.as_view())
]
