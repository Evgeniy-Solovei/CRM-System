from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Регистрация в админ панели модели Product."""

    list_display = ["id", "name", "description", "price"]
    list_filter = ["name", "price"]
    search_fields = [
        "name",
    ]
    ordering = ["name", "price"]
    exclude = [
        "uuid",
    ]
