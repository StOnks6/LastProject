from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

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

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    
    

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    template_name = "recipes_django/recipe_update.html"
    fields = ['title', 'description']
    
    def test_func(self):
        recipe = get_object_or_404(models.Recipe, pk=self.kwargs['pk'])
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author
  

def about_page(request):
    return render(request, "django_recipes/about.html", {"title": "about page"})