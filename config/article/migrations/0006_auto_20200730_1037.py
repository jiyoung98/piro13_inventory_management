# Generated by Django 3.0.8 on 2020-07-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200730_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
