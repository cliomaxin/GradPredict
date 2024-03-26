# Generated by Django 5.0.3 on 2024-03-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="details",
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
                ("student_name", models.CharField(max_length=150)),
                ("admission_number", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
            ],
        ),
    ]
