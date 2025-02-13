# Generated by Django 5.1.4 on 2025-02-06 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("whatsapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("wa_id", models.CharField(max_length=15, unique=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "display_phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WhatsAppMedia",
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
                    "media_type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("video", "Video"),
                            ("audio", "Audio"),
                            ("document", "Document"),
                        ],
                        help_text="Type of the media file",
                        max_length=50,
                    ),
                ),
                (
                    "media_url",
                    models.URLField(
                        blank=True,
                        help_text="URL of the media file, if applicable",
                        null=True,
                    ),
                ),
                (
                    "media_file",
                    models.FileField(
                        blank=True,
                        help_text="Uploaded media file",
                        null=True,
                        upload_to="whatsapp_media/",
                    ),
                ),
                (
                    "media_mime_type",
                    models.CharField(
                        blank=True,
                        help_text="MIME type of the media file",
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WhatsAppMessage",
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
                    "message_type",
                    models.CharField(
                        choices=[
                            ("text", "Text"),
                            ("image", "Image"),
                            ("video", "Video"),
                            ("audio", "Audio"),
                            ("document", "Document"),
                            ("sticker", "Sticker"),
                            ("location", "Location"),
                            ("contact", "Contact"),
                        ],
                        default="text",
                        help_text="Type of the message",
                        max_length=50,
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="Text content of the message, if applicable",
                        null=True,
                    ),
                ),
                (
                    "caption",
                    models.TextField(
                        blank=True,
                        help_text="Caption for media messages, if applicable",
                        null=True,
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp of when the message was sent/received",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("sent", "Sent"),
                            ("failed", "Failed"),
                            ("delivered", "Delivered"),
                            ("read", "Read"),
                        ],
                        default="pending",
                        help_text="Current status of the message",
                        max_length=20,
                    ),
                ),
                (
                    "is_forwarded_to_main_system",
                    models.BooleanField(
                        default=False,
                        help_text="Flag to track if the message was forwarded to the main system",
                    ),
                ),
                (
                    "media",
                    models.ForeignKey(
                        blank=True,
                        help_text="Linked media file",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="whatsapp.whatsappmedia",
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to="whatsapp.contact",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to="whatsapp.contact",
                    ),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
        migrations.CreateModel(
            name="WhatsAppResponse",
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
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to="whatsapp.whatsappmessage",
                    ),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
        migrations.CreateModel(
            name="WhatsAppConversation",
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
                    "contact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conversations",
                        to="whatsapp.contact",
                    ),
                ),
                (
                    "messages",
                    models.ManyToManyField(
                        related_name="conversations", to="whatsapp.whatsappmessage"
                    ),
                ),
                (
                    "responses",
                    models.ManyToManyField(
                        related_name="conversations", to="whatsapp.whatsappresponse"
                    ),
                ),
            ],
        ),
    ]
