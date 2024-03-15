from advertising_company.models import AdvertisingCompany
from django.db import models


class PotentialClient(models.Model):
    """Модель PotentialClient представляет информацию об потенциальном клиенте компании."""

    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"
        ordering = [
            "full_name",
        ]

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone = models.PositiveIntegerField(unique=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")
    advertising_company = models.ForeignKey(
        AdvertisingCompany,
        on_delete=models.CASCADE,
        related_name="potential_clients",
        verbose_name="Рекламная компания",
    )

    def __str__(self):
        return self.full_name
