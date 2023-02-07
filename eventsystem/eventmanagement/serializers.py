from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user = serializers.CharField(read_only=True)
    event_type = serializers.IntegerField(source='event_type_id')
    info = serializers.JSONField()
    timestamp = serializers.DateTimeField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
