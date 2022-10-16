from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'
urlpatterns = [


    #path('logout/', LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.register, name='register')

]
