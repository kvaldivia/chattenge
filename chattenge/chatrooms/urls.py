from django.urls import path

from chattenge.chatrooms.views import (
    chatroom_view,
)

app_name = "chatrooms"
urlpatterns = [
    path("<int:user_id>/chatrooms", view=chatroom_view, name="list"),
]
