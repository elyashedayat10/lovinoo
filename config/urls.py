from django.urls import path, include

from config.api.urls import urlpatterns

app_name = 'confi'

urlpatterns = [
    path('api/', include(urlpatterns)),
]
