from django.db import models

from chattenge.users.models import User


class Chatroom(models.Model):

    name = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=200, default="")
    members = models.ManyToManyField(User)
