from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import ChatModel, Group, GroupChat, DeletedMessages
from django.contrib.auth.decorators import login_required
from .forms import GroupForm, addRemoveToGroupForm
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
    return render(request, 'index.html', context={'users': users, 'groups': groups, 'user': user})


@login_required
def chatPage(request, username):
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    deleted_messages = DeletedMessages.objects.filter(
        username=request.user.username, thread_name=thread_name)
    message_ids = []
    for obj in deleted_messages:
        message_ids.append(obj.message_id)
    messages = []
    for message in message_objs:
        if message.id not in message_ids:
            messages.append(message)
    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': messages})


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
    deleted_messages = DeletedMessages.objects.filter(
        username=request.user.username, thread_name=thread_name)
    message_ids = []
    for obj in deleted_messages:
        message_ids.append(obj.message_id)
    messages = []
    for message in message_objs:
        if message.id not in message_ids:
            messages.append(message)

    return render(request, 'group_chat.html', context={'messages': messages, 'groups': groups, 'group': group})


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


@login_required
def addRemoveToGroup(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method != 'POST':
        form = addRemoveToGroupForm(instance=group)
    else:
        form = addRemoveToGroupForm(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('texting:group', args=[group.id]))

    return render(request, 'add_remove_group_member.html', context={'form': form, 'group_id': group.id})


@login_required
def deleteMessage(request, thread_name, message_id):
    DeletedMessages.objects.create(
        message_id=message_id, thread_name=thread_name, username=request.user.username)
    if thread_name[:5] == 'group':
        group_id = int(thread_name[6:])
        return HttpResponseRedirect(reverse('texting:group', args=[group_id]))
    else:
        user_lst = thread_name[5:].split("-")
        user_id = request.user.id
        if user_id != int(user_lst[0]):
            other_user_id = int(user_lst[0])
        else:
            other_user_id = int(user_lst[1])

        username = User.objects.get(id=other_user_id).username

        return HttpResponseRedirect(reverse('texting:chat', args=[username]))
