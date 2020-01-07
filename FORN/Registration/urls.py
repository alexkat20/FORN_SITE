from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.LogOut.as_view()),
]