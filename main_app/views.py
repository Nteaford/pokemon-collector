from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import GymBadge, Pokemon, HiddenMachine
from .forms import GymBadgeForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemon_index(request):
  pokemons = Pokemon.objects.order_by('name')
  return render(request, 'pokemon/index.html', { 'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  gym_badge_form = GymBadgeForm()
  return render(request, 'pokemon/detail.html', {'pokemon': pokemon, 'gym_badge_form': gym_badge_form})

def add_badge(request, pokemon_id):
  form = GymBadgeForm(request.POST)
  if form.is_valid():
    new_badge = form.save(commit = False)
    new_badge.pokemon_id = pokemon_id
    new_badge.save()
  return redirect('detail', pokemon_id = pokemon_id)

def remove_badge(request, badge_id, pokemon_id):
  GymBadge.objects.get(id=badge_id).pokemon.remove(pokemon_id)
  return redirect('detail', pokemon_id = pokemon_id)

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['pokedex_number', 'classification', 'type1', 'type2', 'generation']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemon/'

class HiddenMachineList(ListView):
  model = HiddenMachine

class HiddenMachineDetail(DetailView):
  model = HiddenMachine

class HiddenMachineCreate(CreateView):
  model = HiddenMachine
  fields = '__all__'

class HiddenMachineUpdate(UpdateView):
  model = HiddenMachine
  fields = ['name', 'color']

class HiddenMachineDelete(DeleteView):
  model = HiddenMachine
  success_url = '/hiddenmachine/'