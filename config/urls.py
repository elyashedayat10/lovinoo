from django.urls import include, path

from config.api.urls import urlpatterns

app_name = "confi"

urlpatterns = [
    path("api/", include(urlpatterns)),
]
