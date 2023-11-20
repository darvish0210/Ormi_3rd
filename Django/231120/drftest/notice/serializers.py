from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Notice


class NoticeSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # views.py를 통해 전달받은 author(= views.py의 NoticeViewSet의 perform_create의 self.request.user)

    class Meta:
        model = Notice
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]