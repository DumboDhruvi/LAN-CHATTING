# chat/urls.py

from django.urls import path
from .views import home_view, group_chat_view  # Import your views

urlpatterns = [
    path('', home_view, name='home'),               # URL for the home page
    path('group/<str:group_name>/<str:username>/', group_chat_view, name='group_chat'),  # URL for group chat
]
