from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import Http404 
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home_page(request):
    recipes = models.Recipe.objects.all()
    context = {
        "recipes": recipes
    }

    return render(request, "django_recipes/home.html", context)


class RecipeList(ListView):
    model = models.Recipe
    template_name = "recipes_django/home.html"
    context_object_name = "recipes"

class RecipeDetail(DetailView):
    model = models.Recipe

class RecipeCreate(LoginRequiredMixin , CreateView):
    model = models.Recipe
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description']
    
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  

def about_page(request):
    return render(request, "django_recipes/about.html", {"title": "about page"})