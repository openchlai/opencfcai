# Generated by Django 5.1.4 on 2025-02-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Email",
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
                ("sender", models.CharField(max_length=255)),
                ("recipient", models.CharField(max_length=255)),
                ("subject", models.TextField()),
                ("body", models.TextField()),
                ("received_date", models.DateTimeField()),
                ("is_read", models.BooleanField(default=False)),
            ],
        ),
    ]
