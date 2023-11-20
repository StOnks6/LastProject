
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.RecipeList.as_view(), name="home-page"),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view(), name="recipes-detail"),
    path('recipe/create/', views.RecipeCreate.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update/', views.UpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about_page, name="about-page")
]
