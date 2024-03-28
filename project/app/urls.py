from django.urls import path
from . import views

urlpatterns = [
    path('members/<int:id>', views.members, name='members'),
    path('emotion',views.emotion,name='emotion'),
    path('chat',views.chat,name="chat"),
]