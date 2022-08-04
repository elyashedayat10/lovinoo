from django.urls import include, path

from activity.api.urls import urlpatterns

app_name = "activity"
urlpatterns = [path("api/", include(urlpatterns))]
