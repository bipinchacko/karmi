from django.urls import path
from chat import views

urlpatterns = [
    path("<int:pk>", views.chatroom, name = "chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),
    path("messageDelete/", views.messageDelete, name="messageDelete"),
    # path("switchUser/", views.switchUser, name="switchUser"),
    path("groupchatroom/<int:pk>", views.groupchatroom, name = "groupchatroom"),
    path("groupchatroom_base/", views.groupchatroom_base, name = "groupchatroom_base"),
    path("ajax_load_messages_group/<int:pk>/", views.ajax_load_messages_group, name="ajax_load_messages_group"),
    path("messageDelete_group/", views.messageDelete_group, name="messageDelete_group"),
]