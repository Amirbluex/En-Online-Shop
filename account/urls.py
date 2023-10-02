from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [

    path('login', views.UserLogin.as_view(), name='user_login'),
    path('register', views.RegisterView.as_view(), name='user_register'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('add/information', views.AddInformation.as_view(), name='add_information'),
    path('logout', views.user_logout, name='user_logout'),

]
