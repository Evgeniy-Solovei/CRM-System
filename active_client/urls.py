from django.urls import path

from .views import (ActiveClientCreateView, ActiveClientDeleteView,
                    ActiveClientDetailView, ActiveClientListView,
                    ActiveClientUpdateView)

urlpatterns = [
    path("list/", ActiveClientListView.as_view(), name="client-list"),
    path("create/", ActiveClientCreateView.as_view(), name="client-create"),
    path("detail/<int:pk>/", ActiveClientDetailView.as_view(), name="client-detail"),
    path("edit/<int:pk>/", ActiveClientUpdateView.as_view(), name="client-edit"),
    path("delete/<int:pk>/", ActiveClientDeleteView.as_view(), name="client-delete"),
]
