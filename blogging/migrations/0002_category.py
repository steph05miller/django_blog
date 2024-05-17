# Generated by Django 5.0.4 on 2024-05-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0001_initial"),
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
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                ("posts", models.ManyToManyField(blank=True, to="blogging.post")),
            ],
        ),
    ]
