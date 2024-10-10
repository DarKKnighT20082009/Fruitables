from django.urls import path

from shop.views import HomePageView, ProductListView, ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('shop/', ProductListView.as_view(), name="shop_page"),
    path('shop/<slug:slug>/', ProductDetailView.as_view(), name="detail_page"),

]