from django.db import models

from chattenge.users.models import User


class Chatroom(models.Model):

    members = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING)
