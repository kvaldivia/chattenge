from django.apps import apps
from chattenge.utils.db import get_typename_for_model_instance

from . import middleware as mw
from . import events


def on_save_any_model(sender, instance, created, **kwargs):
    # We only send updates for chatrooms
    if not hasattr(instance, "chatroom_id"):
        return
    content_type = get_typename_for_model_instance(instance)

    # Ignore any other events
    app_config = apps.get_app_config("chatrooms")
    if content_type not in app_config.events_watched_types:
        return

    sesionid = mw.get_current_session_id()

    type = "change"
    if created:
        type = "create"

    events.emit_event_for_model(instance, sessionid=sesionid, type=type)
