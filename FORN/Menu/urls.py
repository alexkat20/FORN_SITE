from django.urls import path

from . import views

app_name = 'Menu'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.choose_menu, name='choose_menu'),
    path('my_menu/<int:menu_id>', views.see_menu, name='see_menu'),
]
