from django.urls import path

from .views import TariffListApiView

urlpatterns = [
    path('', TariffListApiView.as_view())
]
