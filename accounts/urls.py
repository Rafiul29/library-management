from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('profile/',views.UserBankAccountUpdateView.as_view(),name='profile'),
    path('profile/password_change/',views.PasswordChangeView.as_view(),name='password_change'),
]
