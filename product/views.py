from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category
