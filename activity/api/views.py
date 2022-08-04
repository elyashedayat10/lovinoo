from rest_framework import generics, permissions, status
from rest_framework.response import Response

from profiles.api.serializers import ProfileMainSerializer
from profiles.models import Profile

from ..models import Block, Favorite, Pined, ReportedUser
from .serializers import (BlockCreateSerializer, FavoriteSerializer,
                          ReportedUserSerializers)


class ReportListApiView(generics.ListAPIView):
    serializer_class = ProfileMainSerializer

    def get_queryset(self):
        reported_list = self.request.user.activity_reporteduser_from.all().values_list(
            "to_user", flat=True
        )
        return Profile.objects.filter(user_id__in=reported_list)


    def list(self, request, *args, **kwargs):
        response=super().list(request,*args,**kwargs)
        return Response({
            'is_done': True,
            'message': 'reported profile list',
            'data': response.data
        })



class ReportCreateApiView(generics.CreateAPIView):
    serializer_class = ReportedUserSerializers


    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

    def create(self, request, *args, **kwargs):
        response=super().create(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'کاربر با موفقیت report شد',
            'data':response.data
        })



class FavoriteListApiView(generics.ListAPIView):
    serializer_class = ProfileMainSerializer

    def get(self, request, *args, **kwargs):
        favorite_list = request.user.activity_favorite_from.all().values_list(
            "to_user", flat=True
        )
        favorite_profile = Profile.objects.filter(user_id__in=favorite_list)
        serializer = self.serializer_class(favorite_profile, many=True)
        data = {
            "is_done": True,
            "message": "لیست کاربران مورد علاقه مورد علاقه",
            "data": serializer.data,
        }
        return Response(data=data, status=status.HTTP_200_OK)


class AddTOFavoriteApiView(generics.GenericAPIView):
    serializer_class = FavoriteSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(from_user=request.user)
                context = {
                    "is_done": True,
                    "message": "کاربر به لیست کاربران مورد علاقه اضاغه شد",
                    "data": serializer.data,
                }
                return Response(data=context, status=status.HTTP_201_CREATED)
        except:
            context = {
                "is_done": False,
                "message": "خطلا در انجام عملیات",
            }
            return Response(data=context, status=status.HTTP_406_NOT_ACCEPTABLE)


class RemoveFromFavoriteApiView(generics.GenericAPIView):
    serializer_class = FavoriteSerializer

    def delete(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                to_user = serializer.validated_data["to_user"]
                block_obj = Favorite.objects.get(
                    from_user=request.user, to_user_id=to_user
                )
                block_obj.delete()
                context = {
                    "is_done": False,
                    "message": "کاربر با موفقیت از لیست کاربران موردعلاقه خارج شد",
                }
                return Response(data=context, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            context = {
                "is_done": False,
                "message": 'همچین چیزی نداریم',
            }
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class BlockCreateApiView(generics.CreateAPIView):
    serializer_class = BlockCreateSerializer


    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

    def create(self, request, *args, **kwargs):
        response=super().create(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'کاربر با موفقیت block شد',
            'data':response.data
        })



class BlockListApiView(generics.ListAPIView):
    serializer_class = ProfileMainSerializer

    def get_queryset(self):
        blocked_list = self.request.user.activity_block_from.all().values_list(
            "to_user", flat=True
        )
        return Profile.objects.filter(user_id__in=blocked_list)


    def list(self, request, *args, **kwargs):
        response=super().list(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'لیست کاربران بلاک شده',
            'data':response.data
        })



class BlockRemoveApiView(generics.DestroyAPIView):
    serializer_class = BlockCreateSerializer


    def get_queryset(self):
        blocked_list = self.request.user.activity_block_from.all().values_list(
            "to_user", flat=True
        )
        return Block.objects.filter(fron_user=self.request.user,to_user_id__in=blocked_list)


    def delete(self, request, *args, **kwargs):
        super().delete(request,*args,**kwargs)
        return Response({
            'is_done':True,
            'message':'کاربر از لیست بلاک خارج شد',
        })


