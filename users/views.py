from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from users.models import Profile
from .forms import ProfileForm, RegistrationForm
# Create your views here.


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register'))


def register(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        print(request.POST)
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()

            # authenticated_user = authenticate(
            # username=new_user.username, password=request.POST['password1'])
            #login(request, authenticated_user)
            return HttpResponseRedirect(reverse('users:login'))
            # return HttpResponseRedirect(reverse('logs:index'))
    return render(request, 'register.html', {'form': form})


User = get_user_model()


def profile(request):
    user = User.objects.get(username=request.user.username)
    img_url = user.profile.avatar
    username = user.username
    profile_name = user.profile.profile_name

    return render(request, 'profile_page.html', {"img_url": img_url, "username": username, 'profile_name': profile_name})


def profileUpdate(request):
    if request.method != 'POST':
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
        for f in form:
            print(f)

    else:
        form = ProfileForm(instance=profile, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    return render(request, 'profile_update_page.html', context={'form': form})
