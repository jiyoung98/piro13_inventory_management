# Generated by Django 3.0.8 on 2020-07-29 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.Account', verbose_name='거래처'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='상품 설명'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=25, verbose_name='상품 이름'),
        ),
    ]
