from advertising_company.models import AdvertisingCompany
from django.db import models
from django.db.models import Case, F, FloatField, Sum, When
from django.views.generic import ListView


class StatisticListView(ListView):
    """
    Представление, отображающее рекламные компании и их статистику.
    """

    model = AdvertisingCompany
    context_object_name = "company_statistics"
    template_name = "company_statistics/ads-statistic.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            leads_count=models.Count("potential_clients"),
            active_clients_count=models.Count("potential_clients__activeclient"),
            income=Sum(F("potential_clients__activeclient__contract__price")),
            expenses=Sum("budget", output_field=FloatField()),
        )
        queryset = queryset.annotate(
            success_ratio=Case(
                When(expenses=0, then=0),
                default=F("income") / F("expenses"),
                output_field=FloatField(),
            )
        )
        return queryset
