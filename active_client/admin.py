from active_client.models import ActiveClient
from django.contrib import admin


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    """Регистрация в админ панели модели ActiveClient."""

    list_display = ["id", "potential_client", "contract"]
    list_filter = [
        "id",
    ]
    search_fields = ["potential_client", "contract"]
    ordering = ["potential_client", "contract"]
