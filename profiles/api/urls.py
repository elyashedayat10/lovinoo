from django.urls import path

from .views import ProfileApiView, UserImageUploadApiView, ImageDeleteApiView,ProfileListApiView

urlpatterns = [
    path('', ProfileApiView.as_view()),
    path('list/',ProfileListApiView.as_view()),
    path('upload_image/', UserImageUploadApiView.as_view()),
    path('delete_image/<int:pk>/',ImageDeleteApiView.as_view(),)
]
