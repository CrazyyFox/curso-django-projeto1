from django.shortcuts import render
from recipes.utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.get(id=id),
        'is_detail_page': True,
    })