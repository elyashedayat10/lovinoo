from .serializers import AboutUsSerializer, RulesSerializer

from ..models import AboutUs, Rules

from rest_framework import generics, status
from rest_framework.response import Response


class AboutUsApiView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.first()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        context = {
            'is_done': True,
            'message': 'متن درباره ما',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)


class RuleApiView(generics.GenericAPIView):
    serializer_class = RulesSerializer
    queryset = Rules.objects.first()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        context = {
            'is_done': True,
            'message': 'متن قوانین',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)
