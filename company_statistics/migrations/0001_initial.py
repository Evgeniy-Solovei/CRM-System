# Generated by Django 4.2 on 2024-02-10 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("active_client", "0001_initial"),
        ("passive_client", "0001_initial"),
        ("contract", "0001_initial"),
        ("advertising_company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Statistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "active_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="active_client.activeclient",
                        verbose_name="Активный клиент",
                    ),
                ),
                (
                    "advertising_expense",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="advertising_company.advertisingcompany",
                        verbose_name="Расход от рекламы",
                    ),
                ),
                (
                    "contract_income",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="contract.contract",
                        verbose_name="Доход от контракта",
                    ),
                ),
                (
                    "potential_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statistics",
                        to="passive_client.potentialclient",
                        verbose_name="Потенциальный клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статистика",
                "verbose_name_plural": "Статистики",
            },
        ),
    ]
