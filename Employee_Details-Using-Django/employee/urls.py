from django.urls import path
from . import views

urlpatterns = [
    path('addandshow/', views.addandshow, name='addandshow'),
    path('update/<int:id>/', views.update_data, name='updatedata'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
]