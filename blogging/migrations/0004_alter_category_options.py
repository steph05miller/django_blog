# Generated by Django 5.0.4 on 2024-05-01 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0003_alter_category_posts"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
