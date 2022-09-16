from django.urls import path, include
from . import views
app_name = 'texting'
urlpatterns = [
    path('', views.index, name='home'),
    path('chat/<str:username>/', views.chatPage, name='chat'),
    path('group/<int:group_id>/', views.groupPage, name='group'),
    path('creategroup/', views.createGroup, name='creategroup'),
]
