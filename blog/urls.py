from django.urls import path
from . import views

urlpatterns = [
    path("", views.filteredPosts, name="index"),
    path("posts", views.filteredPosts, name="filtered_posts"),
    path("posts/<str:category>", views.filteredPosts, name="filtered_posts"),
    path("categorias", views.categories, name="categories"),
    path("resumen", views.summary, name="summary"),
    path("post/<int:post>", views.post, name="post"),
]