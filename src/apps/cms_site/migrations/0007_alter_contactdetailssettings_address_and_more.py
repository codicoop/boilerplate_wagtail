# Generated by Django 4.0.7 on 2022-08-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_site', '0006_alter_socialmediaiconssettings_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetailssettings',
            name='address',
            field=models.TextField(blank=True, default='C/ Priora Xixilona, 14<br>\n        08530 La Garriga<br>\n        Barcelona', help_text='Address', null=True),
        ),
        migrations.AlterField(
            model_name='contactdetailssettings',
            name='email',
            field=models.EmailField(blank=True, default='info@moblesciurans.com', help_text='Contact e-mail', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactdetailssettings',
            name='phone',
            field=models.CharField(blank=True, default='93 871 80 07', help_text='Phone number', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediaiconssettings',
            name='vimeo',
            field=models.URLField(blank=True, default='https://vimeo.com/moblesciurans', help_text='Vimeo URL', null=True),
        ),
    ]
