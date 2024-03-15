from django.urls import path

from .views import (ActiveClientsListView, ProductCreateView,
                    ProductDeleteView, ProductDetailView, ProductsListView,
                    ProductUpdateView)

urlpatterns = [
    path("clients_list/", ActiveClientsListView.as_view(), name="clients-list"),
    path("list/", ProductsListView.as_view(), name="products-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("edit/<int:pk>/", ProductUpdateView.as_view(), name="product-edit"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product-delete"),
]
