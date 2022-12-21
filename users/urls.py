from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users'
urlpatterns = [


    #path('logout/', LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    #path('profile_update/', views.profileUpdate, name='profile_update'),

]
