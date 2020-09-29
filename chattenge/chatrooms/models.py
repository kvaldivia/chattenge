from django.db import models

from chattenge.users.models import User


class Chatroom(models.Model):

    name = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=200, default="")
    members = models.ManyToManyField(User)


class Message(models.Model):

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.DO_NOTHING)
    content = models.TextField(null=False)
    sent = models.DateTimeField(auto_now=True)

