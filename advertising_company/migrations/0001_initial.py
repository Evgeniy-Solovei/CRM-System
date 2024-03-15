# Generated by Django 4.2 on 2024-02-10 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertisingCompany",
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
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Название рекламной компании"
                    ),
                ),
                (
                    "promotion",
                    models.CharField(max_length=255, verbose_name="Канал продвижения"),
                ),
                (
                    "budget",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="Бюджет на рекламу",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="Описание услуги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рекламная компания",
                "verbose_name_plural": "Рекламные компании",
                "ordering": ["name"],
            },
        ),
    ]