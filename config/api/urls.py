from django.urls import path

from .views import (AboutUsApiView, CityListApiView, ContactUsCreateAPiView,
                    RuleApiView)

app_name = "config"
urlpatterns = [
    path("rule/", RuleApiView.as_view()),
    path("about_us/", AboutUsApiView.as_view()),
    path('city_list/', CityListApiView.as_view()),
    path('contact_us/', ContactUsCreateAPiView.as_view()),
]
