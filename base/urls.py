from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('rooms/',views.rooms, name='Rooms'),
    path('login/',views.login, name='Login'),
    path('signup/',views.signup, name='Signup')
]