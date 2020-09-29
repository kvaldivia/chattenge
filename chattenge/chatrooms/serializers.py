from rest_framework import serializers, exceptions

from chattenge.chatrooms.models import Message
from chattenge.users.models import User


class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("name",)

class MessageSerializer(serializers.ModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Message
        fields = "__all__"


_SERIALIZERS = {
    Message._meta.verbose_name: MessageSerializer,
    User._meta.verbose_name: UserSerializer,
}


def get_serializer(cls_verbose_name: str) -> serializers.ModelSerializer :

    return _SERIALIZERS.get(cls_verbose_name)
