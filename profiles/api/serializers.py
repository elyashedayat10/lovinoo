from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ..models import Image, Profile


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            "id",
            "image",
        )
        read_only_fields = ("id",)



class ProfileMainSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "user_name",
            "province",
            "city",
            "first_name",
            "last_name",
            "bio",
            "gender",
            "birthdate",
            "user_age",
            "profile_image",
            "status",
        )
        read_only_fields = (
            "user",
            "user_age",
            "status",
            "profile_image",
        )
    def get_profile_image(self, obj):
        profile_image = Image.objects.filter(user=obj.user)
        return ProfileImageSerializer(instance=profile_image, many=True).data

class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField(read_only=True)
    # user=serializers.SerializerMethodField(source='user',read_only=True)
    # liked=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "user_name",
            "province",
            "city",
            "first_name",
            "last_name",
            "bio",
            "gender",
            "birthdate",
            "user_age",
            "profile_image",
            "status",
            # 'liked',
        )
        read_only_fields = (
            "user",
            "user_age",
            "status",
            # 'liked',
        )

    def get_profile_image(self, obj):
        profile_image = Image.objects.filter(user=obj.user)
        return ProfileImageSerializer(instance=profile_image, many=True).data

    # def get_liked(self,obj):
    #     user =  self.context['request'].user
    #     if obj.user in user.activity_favorite_from.all():
    #         return True
    #     return False


class ImageSerializer(serializers.Serializer):
    image = Base64ImageField()


