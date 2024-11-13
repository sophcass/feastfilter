from django.urls import path
from . import views

urlpatterns = [
    path("chatbot/", views.chat_bot_view, name="chat_bot"),
]