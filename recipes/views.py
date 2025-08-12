from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    return HttpResponse("<h1>Bem-vindo à página de receitas!</h1>")

# recipes/views.py
from django.shortcuts import render, get_object_or_404

from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})
def recipe_detail(request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})