# Generated by Django 4.1.4 on 2022-12-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("demo_link", models.CharField(blank=True, max_length=2000, null=True)),
                (
                    "source_link",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
