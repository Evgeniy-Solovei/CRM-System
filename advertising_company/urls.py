from django.urls import path

from .views import (CompanyCreateView, CompanyDeleteView, CompanyDetailView,
                    CompanyListView, CompanyUpdateView)

urlpatterns = [
    path("list/", CompanyListView.as_view(), name="company-list"),
    path("create/", CompanyCreateView.as_view(), name="company-create"),
    path("detail/<int:pk>/", CompanyDetailView.as_view(), name="company-detail"),
    path("edit/<int:pk>/", CompanyUpdateView.as_view(), name="company-edit"),
    path("delete/<int:pk>/", CompanyDeleteView.as_view(), name="company-delete"),
]
