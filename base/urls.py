from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('rooms/',views.rooms, name='Rooms'),
    path('authentication/',views.auth_page, name='auth_page'),
    path('user_login/',views.user_login, name='User_login'),
    path('user_signup/',views.user_signup, name='User_signup'),
]