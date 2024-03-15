from contract.models import Contract
from django.db import models
from passive_client.models import PotentialClient


class ActiveClient(models.Model):
    """Модель ActiveClient предоставляет возможность перевести из пассивного клиента в активного"""

    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"
        ordering = [
            "potential_client__full_name",
        ]

    potential_client = models.OneToOneField(
        PotentialClient, on_delete=models.CASCADE, verbose_name="Клиент"
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="active_clients",
        verbose_name=" Контракт",
    )

    def __str__(self):
        return f"{self.potential_client.full_name} - {self.contract.name}"
