import abc
import importlib

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

from chattenge.utils import importtools as utils


class BaseEventsPushBackend(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def emit_event(self, message: str, *, routing_key: str, channel: str = "events"):
        pass


def get_events_backend(path: str = None, options: dict = None):
    if path is None:
        path = getattr(settings, "EVENTS_PUSH_BACKEND", None)

        if path is None:
            raise ImproperlyConfigured("Events push system not configured")

    if options is None:
        options = getattr(settings, "EVENTS_PUSH_BACKEND_OPTIONS", {})

    cls = utils.load_class(path)
    return cls(**options)
