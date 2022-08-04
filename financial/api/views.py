from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ..models import Tariff
from .serializers import TariffSerializer


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
