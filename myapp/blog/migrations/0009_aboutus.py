# Generated by Django 5.1.3 on 2024-11-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
            ],
        ),
    ]
