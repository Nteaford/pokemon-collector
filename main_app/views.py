from django.shortcuts import render
from django.http import HttpResponse
from .models import pokemons as pokemons

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  return render(request, 'pokemon/index.html', { 'pokemons': pokemons})