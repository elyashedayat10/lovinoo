from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import generics, permissions, status
from rest_framework.response import Response

# from .filters import ProfileFilterSet
from utils.city import cities

from ..models import Image, Profile
from .permissions import OwnerPermissions
from .serializers import (ImageSerializer, ProfileImageSerializer,
                          ProfileSerializer)

user = get_user_model()


class ProfileApiView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.user.profile,context={'request':request})
        context = {
            'is_done': True,
            'message': 'اطاعات کاربر برای شما ارسال شد',
            'data': serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(instance=request.user.profile, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                context = {
                    'is_done': True,
                    'message': 'اطاعات کاربر با موفقیت به روزرسانی شد',
                    'data': serializer.data
                }
                return Response(data=context, status=status.HTTP_200_OK)
        except:
            context = {
                'is_done': False,
                'message': 'خطا در به روزرسانی کاربر',
            }
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class UserImageUploadApiView(generics.GenericAPIView):
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            image = serializer.validated_data['image']
            Image.objects.create(image=image, user=request.user)
            context = {
                'is_done': True,
                'message': 'عکس با موفقیت اپلود شد',
            }
            return Response(data=context, status=status.HTTP_200_OK)
        context = {
            'is_done': False,
            'message': 'خطلا در اپلود پروفایل',
            'data': serializer.errores
        }
        return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class ImageDeleteApiView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    permission_classes = [OwnerPermissions, ]

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({
            'is_done': True
        })





class ProfileListApiView(generics.ListAPIView):
    
    """
    profile list view, exclude blocked user;
    and search bsae on province
    """
    
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('province',)
    ordering_fields = ['created',]


    def get_queryset(self):
        blocked_list = self.request.user.activity_block_from.all().values_list('to_user', flat=True)
        return Profile.objects.exclude(Q(user_id__in=blocked_list) | Q(user=self.request.user))


    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'is_done':True,
            'message': 'profile list',
            'data': response.data
        })


class ProfileFilterApiView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = Profile.objects.all()

    # def get_queryset(self):
    #     blocked_list = self.request.user.activity_block_from.all().values_list('to_user', flat=True)
    #     return Profile.objects.exclude(Q(user_id__in=blocked_list) | Q(user=self.request.user))

    filter_backends = (filters.DjangoFilterBackend,)
    # filterset_class = ProfileFilterSet



class ProfileSearchApiView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    ordering_fields = ['created', ]

    def get_queryset(self):
        blocked_list = self.request.user.activity_block_from.all().values_list('to_user', flat=True)
        query=Profile.objects.exclude(Q(user_id__in=blocked_list) | Q(user=self.request.user))
        return query.filter(user_name__contains=self.request.query_params.get('user_name'))

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            'is_done': True,
            'message': 'profile list',
            'data': response.data
        })
