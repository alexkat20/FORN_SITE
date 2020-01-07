from django.urls import path

from . import views

app_name = 'Foodbloggers'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:video_id>/leave_comment', views.leave_comment, name='leave_comment'),
]