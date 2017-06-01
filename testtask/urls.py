"""testtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from product import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('category-list-view'), permanent=False)),
    url(r'^products/$', views.CategoryListView.as_view(), name='category-list-view'),
    url(r'^products/added-last-day/$', views.AddedLastDayProductsListView.as_view(), name='added-last-day-products-list-view'),
    url(r'^products/(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name='category-detail-view'),
    url(r'^products/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)$', views.ProductDetailView.as_view(), name='product-detail-view'),
    url(r'^admin/', admin.site.urls),
]
