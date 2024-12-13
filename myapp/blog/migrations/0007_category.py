# Generated by Django 5.1.3 on 2024-11-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_post_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
