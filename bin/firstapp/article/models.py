# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Article(models.Model):
    class Meta():
        db_table = 'article'
        verbose_name = 'Статью'

    article_title = models.CharField(max_length=200, verbose_name='Заголовок')
    article_text = models.TextField(verbose_name='Текст статьи')
    article_date = models.DateTimeField(verbose_name="Дата публикации")
    article_likes = models.IntegerField(default=0, verbose_name='Колличество лайков') #(blank=True, null=True)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(verbose_name='Текст коментария')
    comments_article = models.ForeignKey(Article)
