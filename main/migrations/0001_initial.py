# Generated by Django 3.2.7 on 2021-09-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestTable",
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
                ("date", models.DateField(auto_now_add=True)),
                ("name", models.CharField(max_length=100, verbose_name="Название")),
                ("amount", models.IntegerField(verbose_name="Количество")),
                ("distance", models.FloatField(verbose_name="Расстояние")),
            ],
        ),
    ]
