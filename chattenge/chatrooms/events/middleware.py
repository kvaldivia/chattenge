import threading

_local = threading.local()
_local.session_id = None


def get_current_session_id() -> str:
    """
    Get session id for current request.
    """

    global _local
    if not hasattr(_local, "session_id"):
        raise RuntimeError("No session identifier is found")
    return _local.session_id


class SessionIDMiddleware(object):
    """
    Middleware for extract and store a current web sesion
    identifier to thread local storage (that only avaliable for
    current thread).
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)

        return response


    def process_request(self, request):
        global _local
        session_id = request.META.get("HTTP_X_SESSION_ID", None)
        _local.session_id = session_id
        request.session_id = session_id

    def process_response(self, request, response):
        global _local
        _local.session_id = None

        return response
