from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from chattenge.chatrooms.models import Chatroom


User = get_user_model()


class ChatroomListView(LoginRequiredMixin, ListView):

    model = Chatroom

    def get(self, request, *args, **kwargs):
        request.chatrooms = Chatroom.objects.all()
        return super(ChatroomListView, self).get(request, *args, **kwargs)


chatroom_list_view = ChatroomListView.as_view()


class ChatroomView(LoginRequiredMixin, DetailView):

    model = Chatroom


chatroom_view = ChatroomView.as_view()
