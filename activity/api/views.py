from rest_framework import generics, status, permissions
from rest_framework.response import Response
from ..models import Block, Pined, ReportedUser
from .serializers import ReportedUserSerializers, BlockCreateSerializer
from profiles.models import Profile


class ReportListApiView(generics.GenericAPIView):
    serializer_class = ReportedUserSerializers

    def get(self, request, *args, **kwargs):
        reported_list = request.user.activity_reporte_from.all().values_list('id', flat=True)
        # reported_list = ReportedUser.objects.all(from_user=request.user)
        reported_profile = Profile.objects.filter(user_id__in=reported_list)
        serializer = self.serializer_class(data=reported_profile, many=True)
        data = {
            'is_done': True,
            'message': 'لیست گزارش شده  شده',
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)


class ReportCreateApiView(generics.GenericAPIView):
    serializer_class = ReportedUserSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(form_user=request.user)
            data = {"is_done": True, "message": "کاربر گرارش داده  شد", "data": serializer.data}
            return Response(data=data, status=status.HTTP_201_CREATED)
        data = {"is_done": False, "message": "خطلا در انجام عملیات", "data": serializer.errors}
        return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)


class BlockCreateApiView(generics.GenericAPIView):
    serializer_class = BlockCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(from_user=request.user)
            data = {"is_done": True, "message": "کاربر بلاک شد", "data": serializer.data}
            return Response(data=data, status=status.HTTP_201_CREATED)
        data = {"is_done": False, "message": "خطلا در انجام عملیات", "data": serializer.errors}
        return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)


class BlockListApiView(generics.GenericAPIView):
    serializer_class = BlockCreateSerializer

    def get(self, request, *args, **kwargs):
        blocked_user = Block.objects.filter(from_user=request.user).values_list('id', flat=True)
        blocked_profile = Profile.objects.filter(user_id__in=blocked_user)
        serializer = self.serializer_class(data=blocked_profile)
        data = {"is_done": True, "message": "لیست کاربران بلاک شده", "data": serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)


class BlockRemoveApiView(generics.GenericAPIView):
    serializer_class = BlockCreateSerializer

    def delete(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                to_user = serializer.validated_data['to_user']
                block_obj = Block.objects.get(from_user=request.user, to_user_id=to_user)
                block_obj.delete()
                context = {
                    'is_done': False,
                    'message': 'کاربر با موفقیت از لیست بلاک خارج شد',
                }
                return Response(data=context, status=status.HTTP_200_OK)
        except Exception as e:
            context = {
                'is_done': False,
                'message': e,
            }
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
