from django.urls import path

from .views import (ContractCreateView, ContractDeleteView, ContractDetailView,
                    ContractListView, ContractUpdateView)

urlpatterns = [
    path("list/", ContractListView.as_view(), name="contract-list"),
    path("create/", ContractCreateView.as_view(), name="contract-create"),
    path("detail/<int:pk>/", ContractDetailView.as_view(), name="contract-detail"),
    path("edit/<int:pk>/", ContractUpdateView.as_view(), name="contract-edit"),
    path("delete/<int:pk>/", ContractDeleteView.as_view(), name="contract-delete"),
]
