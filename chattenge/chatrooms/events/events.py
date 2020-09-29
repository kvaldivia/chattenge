import json

from django.db import connection

from chattenge.utils.db import get_typename_for_model_instance
from . import middleware as mw
from .backends import base as backends


def emit_event(data: dict, routing_key: str, *,
               sessionid: str = None, channel: str = "events",
               on_commit: bool = True):
    if not sessionid:
        sessionid = mw.get_current_session_id()

    data = {"session_id": sessionid, "data": data}

    backend = backends.get_events_backend()

    def backend_emit_event():
        backend.emit_event(
            message=json.dumps(data),
            routing_key=routing_key,
            channel=channel
        )

    if on_commit:
        connection.on_commit(backend_emit_event)
    else:
        backend_emit_event()


def emit_event_for_model(obj, *, type: str = "change", channel: str = "events",
                         content_type: str = None, sessionid: str = None):
    """
    Sends a model change event.
    """

    assert type in set(["create", "change", "delete"])
    assert hasattr(obj, "chatroom_id")

    if not content_type:
        content_type = get_typename_for_model_instance(obj)

    chatroom_id = getattr(obj, "chatroom_id")
    pk = getattr(obj, "pk", None)

    routing_key = "chatrooms.{0}.message.new".format(chatroom_id)

    data = {
        "type": type,
        "matches": content_type,
        "pk": pk
    }

    return emit_event(
        routing_key=routing_key, channel=channel, sessionid=sessionid,
        data=data)
