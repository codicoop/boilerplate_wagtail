# Generated by Django 4.1.1 on 2023-02-22 15:09

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("cms_site", "0028_aboutuspage_video_description_1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoItem",
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
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=80, verbose_name="Title")),
                ("embed", models.TextField(max_length=255, verbose_name="Embed code")),
                (
                    "description",
                    models.TextField(max_length=255, verbose_name="Description"),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_items",
                        to="cms_site.aboutuspage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
