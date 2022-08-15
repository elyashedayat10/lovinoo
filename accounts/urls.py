from django.urls import include, path

from accounts.api.urls import urlpatterns
from .views import (
    AdminLoginView,
    AddNewAdminView,
    UserDeleteView,
    AdminListView,
    LogoutView,
)

app_name = "accounts"

urlpatterns = [
    path("login/", AdminLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin_list/", AdminListView.as_view(), name="admin_list"),
    path("admin_create/", AddNewAdminView.as_view(), name="admin_create"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete"),
    path("api/", include(urlpatterns)),
]
