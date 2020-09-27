from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from chattenge.chatrooms.models import Chatroom


User = get_user_model()


class ChatroomListView(LoginRequiredMixin, ListView):

    model = Chatroom

    def get(self, request, *args, **kwargs):
        #from pudb import remote as pudb
        #pudb.set_trace(term_size=(213, 55), host='0.0.0.0', port=6900)
        # request.chatrooms = Chatroom.objects.all()
        request.chatrooms = Chatroom.objects.all() 
        return super(ChatroomListView, self).get(request, *args, **kwargs)


chatroom_list_view = ChatroomListView.as_view()


class ChatroomView(LoginRequiredMixin, DetailView,):

    model = Chatroom


chatroom_view = ChatroomView.as_view()
