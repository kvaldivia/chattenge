import importlib

from django.core.exceptions import ImproperlyConfigured


def load_class(path):
    """
    Load class from path.
    """

    mod_name, klass_name = path.rsplit('.', 1)

    try:
        mod = importlib.import_module(mod_name)
    except AttributeError as e:
        raise ImproperlyConfigured('Error importing {0}: "{1}"'.format(mod_name, e))

    try:
        klass = getattr(mod, klass_name)
    except AttributeError:
        raise ImproperlyConfigured('Module "{0}" does not define a "{1}" class'.format(mod_name, klass_name))

    return klass
