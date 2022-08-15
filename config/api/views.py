from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ..models import AboutUs, Rules,Contact
from .serializers import AboutUsSerializer, RulesSerializer,ContactSerializer
from utils.city import cities

class AboutUsApiView(generics.GenericAPIView):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.first()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        context = {"is_done": True, "message": "متن درباره ما", "data": serializer.data}
        return Response(data=context, status=status.HTTP_200_OK)


class RuleApiView(generics.GenericAPIView):
    serializer_class = RulesSerializer
    queryset = Rules.objects.first()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset)
        context = {"is_done": True, "message": "متن قوانین", "data": serializer.data}
        return Response(data=context, status=status.HTTP_200_OK)


# class RuleApiView(ListAPIView):
#     serializer_class = RulesSerializer
#     queryset = Rules.load()
#
#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         return response({
#             "is_done": True
#         })
#
#
# class AboutUsApiView(ListAPIView):
#     queryset = AboutUs.load()
#     serializer_class = AboutUsSerializer
#
#     def list(self, request, *args, **kwargs):
#         response = super().list(request, *args, **kwargs)
#         return response({
#             'is_done': True
#         })



class CityListApiView(generics.GenericAPIView):
    """
    this view is for getting the city of province;
    query params as province passed in views urls and filter down base on that
    """
    def get(self, request, *args, **kwargs):
        province = self.request.query_params.get('province')
        city_list = [item for item in cities if item['state'] == province]
        context = {
            'is_done': True,
            'message': f'لیست شهرهای {province}',
            'city': city_list
        }
        return Response(data=context, status=status.HTTP_200_OK)


class ContactUsCreateAPiView(generics.CreateAPIView):
    """
    this view is for creating contact;
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    def create(self, request, *args, **kwargs):
        response=super().create(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'پیام با موفقیت ارسال شد',
            'data':response.data
        })