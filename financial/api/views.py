from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response

from ..models import Tariff,CartPay
from .serializers import TariffSerializer,CartPaySerializer,PayHistorySerializers


class TariffListApiView(ListAPIView):
    serializer_class = TariffSerializer
    queryset = Tariff.objects.all()

    def list(self, request, *args, **kwargs):
        response=super().list(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'لیست تغرفه ها',
            'data':response.data
        })



class CartPayCreateApiView(CreateAPIView):
    serializer_class = CartPaySerializer
    queryset = CartPay.objects.all()


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


    def create(self, request, *args, **kwargs):
        response=super().create(request, *args, **kwargs)
        return Response({
            'is_done':True,
            'data':response.data
        })

class UserCartPayApiView(ListAPIView):
    serializer_class = CartPaySerializer

    def get_queryset(self):
        cart_pays=self.request.user.cart_pays.all()
        return  cart_pays


    def list(self, request, *args, **kwargs):
        response=super(UserCartPayApiView, self).list(request, *args, **kwargs)
        return Response({
            'is_done':True,
            'data':response.data
        })


class UserHistoryPay(ListAPIView):
    serializer_class = PayHistorySerializers

    def get_queryset(self):
        cart_pays=self.request.user.pays.all()
        return  cart_pays


    def list(self, request, *args, **kwargs):
        response=super(UserHistoryPay, self).list(request, *args, **kwargs)
        return Response({
            'is_done':True,
            'data':response.data
        })