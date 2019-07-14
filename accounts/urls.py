from django.urls import path,include
from . import views
urlpatterns=[
    path('login/',views.login, name='login'),
    path('',views.dashboard, name='dashboard'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logout, name='logout'),
    path('changepassword/',views.change_password,name='change_password'),
    path('resetpassword/',views.reset_password,name='reset_password'),
    path('newpassword/',views.new_password,name='new_password'),
    path('profile/',views.profile,name='profile'),

    path('updateprofile/',views.editprofile, name='update_profile'),
    # path('updateuser/<int:id>/',views.update_user, name='updateuser'),


]