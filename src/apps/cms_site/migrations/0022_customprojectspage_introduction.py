# Generated by Django 4.1.1 on 2023-02-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms_site", "0021_newspage"),
    ]

    operations = [
        migrations.AddField(
            model_name="customprojectspage",
            name="description",
            field=models.TextField(blank=True, default="", verbose_name="description"),
        ),
    ]
