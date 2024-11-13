from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name='home'),  # Home page
    path("chatbot/", views.chat_bot_view, name="chat_bot"),
]