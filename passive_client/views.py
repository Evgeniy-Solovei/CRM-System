from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from passive_client.models import PotentialClient


class PotentialClientsListView(ListView):
    """View для отображения списка потенциальных клиентов."""

    template_name = "passive_client/leads-list.html"
    context_object_name = "leads"

    def get_queryset(self):
        return PotentialClient.objects.select_related("advertising_company").all()


class PotentialClientsDetailView(DetailView):
    """View для детального отображения потенциального клиента."""

    model = PotentialClient
    context_object_name = "lead"
    template_name = "passive_client/leads-detail.html"


class PotentialClientsCreateView(CreateView):
    """View для создания нового потенциального клиента."""

    model = PotentialClient
    fields = ["full_name", "phone", "email", "advertising_company"]
    context_object_name = "lead"
    template_name = "passive_client/leads-create.html"

    def get_success_url(self):
        return reverse_lazy("lead-list")


class PotentialClientsUpdateView(UpdateView):
    """View для обновления информации о потенциальном клиенте."""

    model = PotentialClient
    fields = ["full_name", "phone", "email", "advertising_company"]
    context_object_name = "lead"
    template_name = "passive_client/leads-edit.html"

    def get_success_url(self):
        return reverse_lazy("lead-detail", kwargs={"pk": self.object.pk})


class PotentialClientsDeleteView(DeleteView):
    """View для удаления потенциального клиента."""

    model = PotentialClient
    success_url = reverse_lazy("lead-list")
    context_object_name = "lead"
    template_name = "passive_client/leads-delete.html"
