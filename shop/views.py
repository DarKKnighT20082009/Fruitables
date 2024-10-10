from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop.models import Product, ProductCategory


# Create your views here.
class HomePageView(ListView):
    model = Product
    template_name = "shop/index.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()


class ProductListView(DetailView):
    model = Product
    template_name = "shop/shop.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()
        return context


class ProductDetailView(ListView):
    model = Product
    template_name = "shop/shop-detail.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductCategory.objects.all()
        context["product"] = Product.objects.get(slug=self.kwargs["slug"])
        return context
