from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('pokemon/', views.pokemon_index, name = 'pokemon'),
path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon_update'),
path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon_delete'),
path('pokemon/<int:pokemon_id>/add_badge/', views.add_badge, name='add_badge'),
path('pokemon/<int:pokemon_id>/remove_badge/', views.remove_badge, name='remove_badge'),
  path('hiddenmachine/', views.HiddenMachineList.as_view(), name='hiddenmachine_index'),
  path('hiddenmachine/<int:pk>/', views.HiddenMachineDetail.as_view(), name='hiddenmachine_detail'),
  path('hiddenmachine/create/', views.HiddenMachineCreate.as_view(), name='hiddenmachine_create'),
  path('hiddenmachine/<int:pk>/update/', views.HiddenMachineUpdate.as_view(), name='hiddenmachine_update'),
  path('hiddenmachine/<int:pk>/delete/', views.HiddenMachineDelete.as_view(), name='hiddenmachine_delete'),
]