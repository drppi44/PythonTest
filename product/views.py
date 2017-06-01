from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product
from datetime import datetime, timedelta


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        return get_object_or_404(
            Product,
            category__slug=self.kwargs['category_slug'],
            slug=self.kwargs['product_slug']
        )


class AddedLastDayProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/added_last_day_products_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            created_at__gte=(datetime.now()-timedelta(days=1))
        )
