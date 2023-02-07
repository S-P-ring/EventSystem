import uuid
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_type = models.ForeignKey('EventType', on_delete=models.PROTECT)
    info = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type.name}" + "_" + f"{self.user.username}"

    class Meta:
        verbose_name = 'Events'
        verbose_name_plural = 'Events'


class EventType(models.Model):
    name = models.CharField(unique=True, max_length=256, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Events type'
        verbose_name_plural = 'Events type'
