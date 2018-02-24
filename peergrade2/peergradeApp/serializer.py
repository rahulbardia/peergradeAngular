from rest_framework import serializers
from models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        model = Notification
        fields = ('id', 'created_at', 'sender', 'active', 'content', 'request_moderation')
