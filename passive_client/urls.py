from django.urls import path

from .views import (PotentialClientsCreateView, PotentialClientsDeleteView,
                    PotentialClientsDetailView, PotentialClientsListView,
                    PotentialClientsUpdateView)

urlpatterns = [
    path("list/", PotentialClientsListView.as_view(), name="lead-list"),
    path("create/", PotentialClientsCreateView.as_view(), name="lead-create"),
    path("detail/<int:pk>/", PotentialClientsDetailView.as_view(), name="lead-detail"),
    path("edit/<int:pk>/", PotentialClientsUpdateView.as_view(), name="lead-edit"),
    path("delete/<int:pk>/", PotentialClientsDeleteView.as_view(), name="lead-delete"),
]
