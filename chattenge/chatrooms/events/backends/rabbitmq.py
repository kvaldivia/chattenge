import logging
from urllib.parse import urlparse

import pika

from . import base


log = logging.getLogger("chatroom.events")


def _make_rabbitmq_connection(url):
    parse_result = urlparse(url)
    try:
        (authdata, host) = parse_result.netloc.split("@")
    except Exception as e:
        raise RuntimeError("Invalid url") from e

    try:
        (user, password) = authdata.split(":")
    except Exception:
        (user, password) = ("guest", "guest")

    vhost = parse_result.path
    credentials = pika.PlainCredentials(user, password)
    host, port = host.split(":")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host=vhost[1:],
            credentials=credentials
        )
    )

    return connection


class EventsPushBackend(base.BaseEventsPushBackend):
    def __init__(self, url):
        self.url = url

    def emit_event(self, message: str, *, routing_key: str, channel: str = "events"):
        try:
            connection = _make_rabbitmq_connection(self.url)
            channel = connection.channel()
            channel.queue_declare(queue='messages')
            channel.exchange_declare(exchange='messages', exchange_type='fanout')
        except pika.exceptions.AMQPConnectionError:
            err_msg = """\
                EventsPushBackend: Unable to connect with RabbitMQ\
                (connection refused) at {}""".format(self.url)
            log.error(err_msg, exc_info=True)
        except pika.exceptions.ProbableAccessDeniedError:
            err_msg = """\
                EventsPushBackend: Unable to connect with\
                RabbitMQ (access refused) at {}""".format(self.url)
            log.error(err_msg, exc_info=True)
        else:
            try:
                channel.basic_publish(
                    exchange='messages', body=message, routing_key='messages')
            except Exception:
                log.error(
                    "EventsPushBackend: Unhandled exception", exc_info=True)
            finally:
                connection.close()
