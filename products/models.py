import uuid

from django.db import models


class Product(models.Model):
    """Модель Product представляет информацию об услугах компании."""

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = [
            "name",
        ]

    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена услуги"
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name="UUID"
    )

    def __str__(self):
        return self.name
