from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import ChatModel, Group, GroupChat
from django.contrib.auth.decorators import login_required
from .forms import GroupForm
# Create your views here.
User = get_user_model()


@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    user = User.objects.get(username=request.user.username)
    all_groups = Group.objects.all()
    groups = []
    for group in all_groups:
        if request.user in group.members.all():
            groups.append(group)
    return render(request, 'index.html', context={'users': users, 'groups': groups})


@login_required
def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs})


@login_required
def groupPage(request, group_id):
    all_groups = Group.objects.all()
    groups = []
    for group in all_groups:
        if request.user in group.members.all():
            groups.append(group)
    group = Group.objects.get(id=group_id)
    thread_name = f'group_{group_id}'
    message_objs = GroupChat.objects.filter(thread_name=thread_name)
    return render(request, 'group_chat.html', context={'messages': message_objs, 'groups': groups, 'group': group})


@login_required
def createGroup(request):
    if request.method != 'POST':
        form = GroupForm()

    else:
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.creator = request.user
            new_group.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('texting:home'))
    return render(request, 'create_group.html', context={'form': form})
