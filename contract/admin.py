from contract.models import Contract
from django.contrib import admin


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Регистрация в админ панели модели Contract."""

    list_display = ["id", "name", "product", "file", "start_date", "end_data", "price"]
    list_filter = ["id", "name", "product"]
    search_fields = ["name", "product", "price"]
    ordering = ["name", "product", "start_date", "end_data", "price"]
