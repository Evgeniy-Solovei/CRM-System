from django.db import models
from products.models import Product


class AdvertisingCompany(models.Model):
    """Модель AdvertisingCompany представляет информацию о рекламной компании."""

    class Meta:
        verbose_name = "Рекламная компания"
        verbose_name_plural = "Рекламные компании"
        ordering = [
            "name",
        ]

    name = models.CharField(max_length=255, verbose_name="Название рекламной компании")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Описание услуги"
    )
    promotion = models.CharField(max_length=255, verbose_name="Канал продвижения")
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет на рекламу"
    )

    def __str__(self):
        return self.name
