# Generated by Django 4.1.3 on 2022-12-03 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseUser",
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
                ("full_name", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "ADMIN"),
                            ("OPERATOR LOGISTIK", "OPERATOR LOGISTIK"),
                            ("SALES", "SALES"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdminUser",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="account.baseuser",
                    ),
                ),
            ],
            bases=("account.baseuser",),
        ),
        migrations.CreateModel(
            name="Sales",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="account.baseuser",
                    ),
                ),
                ("order_list", models.JSONField(default=dict)),
                (
                    "created_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.adminuser",
                    ),
                ),
            ],
            bases=("account.baseuser",),
        ),
        migrations.CreateModel(
            name="LogisticOperator",
            fields=[
                (
                    "baseuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="account.baseuser",
                    ),
                ),
                (
                    "created_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.adminuser",
                    ),
                ),
            ],
            bases=("account.baseuser",),
        ),
    ]
