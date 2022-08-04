from django.urls import path

from .views import (ImageDeleteApiView, ProfileApiView, ProfileFilterApiView,
                    ProfileListApiView, ProfileSearchApiView,
                    UserImageUploadApiView)

urlpatterns = [
    path("", ProfileApiView.as_view()),
    path("list/", ProfileListApiView.as_view()),
    path("upload_image/", UserImageUploadApiView.as_view()),
    path(
        "delete_image/<int:pk>/",
        ImageDeleteApiView.as_view(),
    ),
    path('filter/',ProfileFilterApiView.as_view()),
    path('search/',ProfileSearchApiView.as_view())
]
