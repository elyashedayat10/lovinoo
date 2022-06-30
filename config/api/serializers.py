from rest_framework import serializers
from ..models import Rules, AboutUs
from django.utils.safestring import mark_safe


class AboutUsSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = (
            'title',
            'description',
        )

    def get_content(self, obj):
        return mark_safe(obj.description)


class RulesSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Rules
        fields = (
            'title',
            'description',
        )

    def get_content(self, obj):
        return mark_safe(obj.description)
