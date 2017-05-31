from django.views.generic import ListView, DetailView
from .models import Category, Product
from datetime import datetime, timedelta


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class ProductDetailView(DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'


class AddedLastDayProductsListView(ListView):
    model = Product
    template_name = 'product/added_last_day_products_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            created_at__gte=(datetime.now()-timedelta(days=1))
        )
