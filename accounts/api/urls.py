from django.urls import path

from .views import AuthApiView, LogoutApiView, VerifyApiView

urlpatterns = [
    path("auth/", AuthApiView.as_view()),
    path("verify/", VerifyApiView.as_view()),
    path("logout/", LogoutApiView.as_view()),
]
