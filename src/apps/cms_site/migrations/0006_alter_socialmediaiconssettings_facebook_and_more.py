# Generated by Django 4.0.7 on 2022-08-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_site', '0005_socialmediaiconssettings_contactdetailssettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaiconssettings',
            name='facebook',
            field=models.URLField(blank=True, default='https://www.facebook.com/moblesciurans', help_text='Facebook URL', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediaiconssettings',
            name='instagram',
            field=models.URLField(blank=True, default='https://www.instagram.com/moblesciurans', help_text='Instagram URL', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediaiconssettings',
            name='vimeo',
            field=models.URLField(blank=True, default='http://vimeo.com/moblesciurans', help_text='Vimeo URL', null=True),
        ),
        migrations.AlterField(
            model_name='socialmediaiconssettings',
            name='youtube',
            field=models.URLField(blank=True, default='http://www.youtube.com/user/ciuransmobles', help_text='Youtube URL', null=True),
        ),
    ]