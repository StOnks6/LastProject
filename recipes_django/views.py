from django.shortcuts import render
from . import models

# Create your views here.
def home_page(request):
    recipes = models.Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "django_recipes/home.html", context)

def about_page(request):
    return render(request, "django_recipes/about.html", {"title": "about page"})