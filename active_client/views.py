from active_client.models import ActiveClient
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


class ActiveClientListView(ListView):
    """View для отображения списка активных клиентов."""

    template_name = "active_client/customers-list.html"
    context_object_name = "clients"

    def get_queryset(self):
        return ActiveClient.objects.select_related("potential_client", "contract").all()


class ActiveClientDetailView(DetailView):
    """View для детального отображения активного клиента."""

    model = ActiveClient
    context_object_name = "client"
    template_name = "active_client/customers-detail.html"


class ActiveClientCreateView(CreateView):
    """View для создания нового активного клиента."""

    model = ActiveClient
    fields = ["potential_client", "contract"]
    context_object_name = "client"
    template_name = "active_client/customers-create.html"

    def get_success_url(self):
        return reverse_lazy("client-list")


class ActiveClientUpdateView(UpdateView):
    """View для обновления информации об активном клиенте."""

    model = ActiveClient
    fields = ["potential_client", "contract"]
    context_object_name = "client"
    template_name = "active_client/customers-edit.html"

    def get_success_url(self):
        return reverse_lazy("client-detail", kwargs={"pk": self.object.pk})


class ActiveClientDeleteView(DeleteView):
    """View для удаления активного клиента."""

    model = ActiveClient
    success_url = reverse_lazy("client-list")
    context_object_name = "client"
    template_name = "active_client/customers-delete.html"
