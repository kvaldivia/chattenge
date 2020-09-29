from django.apps import apps, AppConfig
from django.db.models import signals
from django.utils.translation import gettext_lazy as _


def connect_events_signals():
    from .events import signal_handlers as handlers
    signals.post_save.connect(handlers.on_save_any_model, dispatch_uid="events_change")


def disconnect_events_signals():
    signals.post_save.disconnect(dispatch_uid="events_change")


class ChatroomsConfig(AppConfig):
    name = "chattenge.chatrooms"
    verbose_name = _("Chatrooms")
    watched_types = ("chatrooms.message",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.events_watched_types = set()

    def ready(self):
        connect_events_signals()
        for config in apps.get_app_configs():
            if not hasattr(config, "watched_types"):
                continue

            self.events_watched_types = self.events_watched_types.union(config.watched_types)
