from django.urls import path
from chat import views

urlpatterns = [
    path("<int:pk>", views.chatroom, name = "chatroom")
]