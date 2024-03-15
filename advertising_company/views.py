from advertising_company.models import AdvertisingCompany
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)


class CompanyListView(ListView):
    """View для отображения списка рекламных компаний."""

    template_name = "advertising_company/ads-list.html"
    context_object_name = "companies"

    def get_queryset(self):
        return AdvertisingCompany.objects.select_related("product").all()


class CompanyDetailView(DetailView):
    """View для детального отображения рекламных компаний."""

    model = AdvertisingCompany
    context_object_name = "company"
    template_name = "advertising_company/ads-detail.html"


class CompanyCreateView(CreateView):
    """View для создания новой рекламной компании."""

    model = AdvertisingCompany
    fields = ["name", "product", "promotion", "budget"]
    context_object_name = "company"
    template_name = "advertising_company/ads-create.html"

    def get_success_url(self):
        return reverse_lazy("company-list")


class CompanyUpdateView(UpdateView):
    """View для обновления информации об рекламной компании."""

    model = AdvertisingCompany
    fields = ["name", "product", "promotion", "budget"]
    context_object_name = "company"
    template_name = "advertising_company/ads-edit.html"

    def get_success_url(self):
        return reverse_lazy("company-detail", kwargs={"pk": self.object.pk})


class CompanyDeleteView(DeleteView):
    """View для удаления рекламной компании."""

    model = AdvertisingCompany
    success_url = reverse_lazy("company-list")
    context_object_name = "company"
    template_name = "advertising_company/ads-delete.html"
