# Generated by Django 4.1.7 on 2023-06-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms_site", "0011_rename_title_collectionitem_title_ca"),
    ]

    operations = [
        migrations.AddField(
            model_name="collectionitem",
            name="title_es",
            field=models.CharField(
                blank=True, default="", max_length=80, verbose_name="Title (spanish)"
            ),
        ),
        migrations.AlterField(
            model_name="collectionitem",
            name="title_ca",
            field=models.CharField(max_length=80, verbose_name="Title (catalan)"),
        ),
    ]
