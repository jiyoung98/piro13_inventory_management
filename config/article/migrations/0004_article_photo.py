# Generated by Django 3.0.8 on 2020-07-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200730_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
