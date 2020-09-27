from django.urls import path

from chattenge.chatrooms.views import (
    chatroom_list_view,
    chatroom_view,
)

app_name = "chatrooms"
urlpatterns = [
    path("all", view=chatroom_list_view, name="list"),
    path("<pk>", view=chatroom_view, name="details"),
    path("<pk>/messages", view=chatroom_view, name="messages"),
]
