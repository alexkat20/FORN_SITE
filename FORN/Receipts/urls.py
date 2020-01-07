from django.urls import path

from . import views

app_name = 'Receipts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receipt_id>/', views.detail, name='detail'),
    path('<int:receipt_id>/leave_comment', views.leave_comment, name='leave_comment'),
    path('new_receipt/', views.create_receipt, name='create_receipt')
]


