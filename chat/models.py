from django.conf import settings
from django.db import models

user = settings.AUTH_USER_MODEL


# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE)
    room = models.ForeignKey(
        'Room',
        related_name='messages',
        on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    room_name = models.CharField(max_length=255)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='rooms')
    created_at = models.DateTimeField(
        verbose_name='Creation Date',
        auto_now_add=True)
    last_activity = models.DateTimeField(
        verbose_name='Last activity date',
        auto_now=True)
