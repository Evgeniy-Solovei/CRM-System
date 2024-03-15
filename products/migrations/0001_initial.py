# Generated by Django 4.2 on 2024-02-10 22:05

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                    models.CharField(max_length=255, verbose_name="Название услуги"),
                ),
                ("description", models.TextField(verbose_name="Описание услуги")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена услуги"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        unique=True,
                        verbose_name="UUID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
                "ordering": ["name"],
            },
        ),
    ]