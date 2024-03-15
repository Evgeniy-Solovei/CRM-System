from advertising_company.models import AdvertisingCompany
from django.contrib import admin


@admin.register(AdvertisingCompany)
class AdvertisingCompanyAdmin(admin.ModelAdmin):
    """Регистрация в админ панели модели AdvertisingCompany."""

    list_display = ["id", "name", "product", "promotion", "budget"]
    list_filter = ["id", "name", "budget"]
    search_fields = ["name", "product", "promotion"]
    ordering = ["name", "promotion", "-budget"]
