from django.db import models
from products.models import Product


class Contract(models.Model):
    """Модель Contract представляет информацию о контракте."""

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
        ordering = [
            "name",
        ]

    name = models.CharField(max_length=255, verbose_name="Название контракта")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="contracts",
        verbose_name="Услуга",
    )
    file = models.FileField(
        upload_to="contract_documents/", verbose_name="Файл с документами"
    )
    start_date = models.DateField(verbose_name="Дата заключения контракта")
    end_data = models.DateField(verbose_name="Дата завершения контракта")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Сумма контракта"
    )

    def __str__(self):
        return self.name
