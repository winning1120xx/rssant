# Generated by Django 2.2.12 on 2020-04-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0021_auto_20200418_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='warnings',
            field=models.TextField(blank=True, help_text='warning messages when processing the feed', null=True),
        ),
    ]
