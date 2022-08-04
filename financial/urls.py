from django.urls import include, path

from financial.api.urls import urlpatterns

app_name = 'financial'
urlpatterns = [
    path('api/', include(urlpatterns))
]
