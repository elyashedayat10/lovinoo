from django.urls import path

from .views import TariffListApiView,CartPayCreateApiView,UserCartPayApiView,UserHistoryPay

urlpatterns = [
    path('', TariffListApiView.as_view()),
    path('cart_pay/', CartPayCreateApiView.as_view()),
    path('user_cart_pay/', UserCartPayApiView.as_view()),
    path('user_pay/', UserHistoryPay.as_view()),
]
