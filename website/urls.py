from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('logout/', views.logout_user, name='logout'),
    path('Register/', views.Register_user, name='register'),
    path('record/<int:pk>', views.record, name='record'),
    path('add/', views.add_record, name='add_record'),
    path('update/<int:pk>', views.update_record, name='update'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
]