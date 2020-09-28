from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from chattenge.chatrooms.models import Chatroom


class JoinChatroomView(APIView):

    permission_classes = [permissions.IsAuthenticated]

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

    class Meta:
        model = Chatroom

    def post(self, request, format=None, *args, **kwargs):
        chatroom_id = kwargs.get('pk')

        if not chatroom_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
        chatroom.members.remove(request.user)
        chatroom.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

leave_chatroom_view = LeaveChatroomView.as_view()
