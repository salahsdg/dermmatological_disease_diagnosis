# Generated by Django 5.0.6 on 2024-05-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predictions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SkinDisease",
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
                ("name", models.CharField(max_length=255)),
                ("symptoms", models.TextField()),
                ("prediction_model", models.FileField(upload_to="models/")),
            ],
        ),
        migrations.DeleteModel(
            name="Prediction",
        ),
    ]
