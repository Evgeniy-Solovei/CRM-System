from active_client.models import ActiveClient
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from products.models import Product


class ActiveClientsListView(ListView):
    """View для отображения списка активных клиентов."""

    template_name = "products/clients-list.html"
    context_object_name = "clients"

    def get_queryset(self):
        return ActiveClient.objects.select_related("potential_client", "contract").all()


class ProductsListView(ListView):
    """View для отображения списка продуктов."""

    template_name = "products/products-list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    """View для детального отображения продукта."""

    model = Product
    context_object_name = "product"
    template_name = "products/products-detail.html"


class ProductCreateView(CreateView):
    """View для создания нового продукта."""

    model = Product
    fields = ["name", "description", "price"]
    context_object_name = "product"
    template_name = "products/products-create.html"

    def get_success_url(self):
        return reverse_lazy("products-list")


class ProductUpdateView(UpdateView):
    """View для обновления информации о продукте."""

    model = Product
    fields = ["name", "description", "price"]
    context_object_name = "product"
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    """View для удаления продукта."""

    model = Product
    success_url = reverse_lazy("products-list")
    context_object_name = "product"
    template_name = "products/products-delete.html"
