# Generated by Django 5.1.4 on 2025-02-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emailfeedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="raw_message",
            field=models.BinaryField(default=None),
        ),
    ]
