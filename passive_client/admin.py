from django.contrib import admin
from passive_client.models import PotentialClient


@admin.register(PotentialClient)
class PotentialClientAdmin(admin.ModelAdmin):
    """Регистрация в админ панели модели PotentialClient."""

    list_display = ["id", "full_name", "phone", "email", "advertising_company"]
    list_filter = ["id", "full_name"]
    search_fields = ["name", "email"]
    ordering = [
        "full_name",
    ]
