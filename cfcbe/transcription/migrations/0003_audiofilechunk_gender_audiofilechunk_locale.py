# Generated by Django 5.1.4 on 2025-02-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transcription", "0002_remove_audiofile_feature_text_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="audiofilechunk",
            name="gender",
            field=models.CharField(
                choices=[
                    ("male", "Male"),
                    ("female", "Female"),
                    ("not_sure", "Not Sure"),
                ],
                default="not_sure",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="audiofilechunk",
            name="locale",
            field=models.CharField(
                choices=[("en", "English"), ("sw", "Swahili"), ("both", "Both")],
                default="both",
                max_length=5,
            ),
        ),
    ]
