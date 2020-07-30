from django.db import models
from django.shortcuts import render, redirect, reverse

class Account(models.Model):
    name = models.CharField(max_length=25)
    call = models.CharField(max_length=25)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Article(models.Model):
    title = models.CharField(max_length=25, verbose_name='상품 이름')
    content = models.TextField(verbose_name='상품 설명')
    photo = models.ImageField(blank=True, upload_to="image")
    price = models.CharField(default=1, max_length=25, verbose_name='가격')
    amount = models.PositiveIntegerField(default=1, verbose_name='수량')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1, verbose_name='거래처')

    def get_absolute_url(self):  # new
        return reverse('article:retrieve', args=[str(self.id)])

    def __str__(self):
        return '{}'.format(self.title)

