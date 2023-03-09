# Generated by Django 4.1.7 on 2023-03-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_data_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(default="", max_length=50, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(default="", max_length=100, verbose_name="Surnames"),
        ),
    ]