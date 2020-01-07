from django.urls import path

from . import views

app_name = 'Master_class'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:video_id>/', views.detail, name='detail'),
    path('<int:video_id>/leave_comment', views.leave_comment, name='leave_comment'),
]
