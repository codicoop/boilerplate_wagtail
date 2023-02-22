# Generated by Django 4.1.1 on 2023-02-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cms_site", "0029_videoitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_1",
        ),
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_2",
        ),
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_3",
        ),
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_4",
        ),
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_5",
        ),
        migrations.RemoveField(
            model_name="aboutuspage",
            name="video_description_6",
        ),
        migrations.AlterField(
            model_name="videoitem",
            name="description",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="videoitem",
            name="embed",
            field=models.TextField(verbose_name="Embed code"),
        ),
    ]