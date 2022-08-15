from django.urls import include, path
from .views import home
from config.api.urls import urlpatterns

app_name = "confi"

urlpatterns = [
    path("api/", include(urlpatterns)),
    path("", home),
]
