from active_client.models import ActiveClient
from advertising_company.models import AdvertisingCompany
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from passive_client.models import PotentialClient
from products.models import Product


class HomeTemplateView(TemplateView):
    """
    Представление, отображающее домашнюю страницу.
    """

    template_name = "user_auth/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()
        context["advertisements_count"] = AdvertisingCompany.objects.count()
        context["leads_count"] = PotentialClient.objects.count()
        context["customers_count"] = ActiveClient.objects.count()
        return context


class UserLoginView(LoginView):
    """
    Представление обрабатывает вход пользователя.
    """

    form_class = AuthenticationForm
    template_name = "user_auth/login.html"

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    """
    Представление обрабатывает выход пользователя.
    """

    def get_success_url(self):
        return reverse_lazy("login")
