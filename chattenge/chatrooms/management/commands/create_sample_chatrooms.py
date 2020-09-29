"""Django command to populate chatroom model."""
import logging

from django.core.management.base import BaseCommand

from chattenge.chatrooms.models import Chatroom

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create sample chatrooms for testing"

    CHATROOMS_DATA = [
        {
            "name": "Chatroom 1",
            "description": "This chatroom is for testing"
        },
        {
            "name": "Chatroom 2",
            "description": "This chatroom is for devs"
        },
        {
            "name": "Meta",
            "description": "For meme sharing only!!!"
        },
    ]

    def handle(self, *args, **options):
        self.stdout.write('Creating chatrooms.')

        for chatroom in self.CHATROOMS_DATA:
            Chatroom.objects.get_or_create(**chatroom)
