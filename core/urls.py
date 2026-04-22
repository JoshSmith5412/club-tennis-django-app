from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_list, name='player_list'), path('add-player/', views.add_player, name='add_player'),
    path('delete-player/<int:id>/', views.delete_player, name='delete_player'),
    path('edit-player/<int:id>/', views.edit_player, name='edit_player'),
]