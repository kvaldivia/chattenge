from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChatroomsConfig(AppConfig):
    name = "chattenge.chatrooms"
    verbose_name = _("Chatrooms")
