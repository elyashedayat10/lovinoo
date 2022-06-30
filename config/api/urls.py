from django.urls import path
from .views import (
    AboutUsApiView,
    RuleApiView,
)

app_name = 'config'
urlpatterns = [
    path('rule/', RuleApiView.as_view()),
    path('about_us/', AboutUsApiView.as_view()),
]
