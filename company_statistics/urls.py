from django.urls import path

from .views import StatisticListView

urlpatterns = [
    path("", StatisticListView.as_view(), name="statistic"),
]
