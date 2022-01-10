from django.shortcuts import render
from django.http import HttpResponse
from .models import pokemons as pokemons

# Create your views here.
def home(request):
  return HttpResponse('Welcome to the Pokemon Center Homepage')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  return render(request, 'pokemon/index.html', { 'pokemons': pokemons})