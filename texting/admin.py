from django.contrib import admin
from .models import ChatModel, Group, GroupChat
# Register your models here.
admin.site.register(ChatModel)
admin.site.register(Group)
admin.site.register(GroupChat)