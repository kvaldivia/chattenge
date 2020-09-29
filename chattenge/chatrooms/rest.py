from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from chattenge.chatrooms.models import Chatroom, Message
from chattenge.chatrooms.serializers import MessageSerializer, CreateMessageSerializer


class JoinChatroomView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    class Meta:
        model = Chatroom

    def post(self, request, format=None, *args, **kwargs):
        chatroom_id = kwargs.get('pk')

        if not chatroom_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
        chatroom.members.add(request.user)
        chatroom.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


join_chatroom_view = JoinChatroomView.as_view()


class LeaveChatroomView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    class Meta:
        model = Chatroom

    def post(self, request, format=None, *args, **kwargs):
        chatroom_id = kwargs.get('pk')
        chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
        chatroom.members.remove(request.user)
        chatroom.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


leave_chatroom_view = LeaveChatroomView.as_view()


class SendMessageView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    class Meta:
        model = Message
        serializer_class = MessageSerializer

    def post(self, request, format=None, *args, **kwargs):
        chatroom_id = kwargs.get('pk')
        chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
        data = {
            **request.data,
            "chatroom": chatroom_id,
            "author": request.user.id,
        }
        serializer = CreateMessageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_428_PRECONDITION_REQUIRED, )


send_message_view = SendMessageView.as_view()
