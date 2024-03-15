from contract.models import Contract
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


class ContractListView(ListView):
    """View для отображения списка контрактов."""

    template_name = "contract/contracts-list.html"
    context_object_name = "contracts"

    def get_queryset(self):
        return Contract.objects.select_related("product").all()


class ContractDetailView(DetailView):
    """View для детального отображения контракта."""

    model = Contract
    context_object_name = "contract"
    template_name = "contract/contracts-detail.html"


class ContractCreateView(CreateView):
    """View для создания нового контракта."""

    model = Contract
    fields = ["name", "product", "file", "start_date", "end_data", "price"]
    context_object_name = "contract"
    template_name = "contract/contracts-create.html"

    def get_success_url(self):
        return reverse_lazy("contract-list")


class ContractUpdateView(UpdateView):
    """View для обновления информации о контракте."""

    model = Contract
    fields = ["name", "product", "file", "start_date", "end_data", "price"]
    context_object_name = "contract"
    template_name = "contract/contracts-edit.html"

    def get_success_url(self):
        return reverse_lazy("contract-detail", kwargs={"pk": self.object.pk})


class ContractDeleteView(DeleteView):
    """View для удаления контракта."""

    model = Contract
    success_url = reverse_lazy("contract-list")
    context_object_name = "contract"
    template_name = "contract/contracts-delete.html"
