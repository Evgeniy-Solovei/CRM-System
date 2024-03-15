from django.urls import path

from .views import HomeTemplateView, UserLoginView, UserLogoutView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
