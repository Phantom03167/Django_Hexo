from django.db import models
from mdeditor.fields import MDTextField
from datetime import datetime,date
from django.utils.html import format_html
import random


# Create your models here.

# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    summary = models.TextField(max_length=100, verbose_name='文章概述')
    cover = models.CharField(max_length=200, default='https://image.3001.net/images/20200304/15832956271308.jpg',
                             verbose_name='文章封面')
    content = MDTextField(verbose_name='文章内容')
    read_count = models.IntegerField(default=0, verbose_name='阅读次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    pub_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.SET_DEFAULT())
    # tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    article_id = models.CharField(max_length=14,
                                  default=date.today().strftime("%Y%m%d") + str(random.randint(0, 999999)).zfill(6),
                                  verbose_name='文章编号', primary_key=True)

    def cover_data(self):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            self.cover,
        )

    def cover_admin(self):
        return format_html(
            '<img src="{}" width="440px" height="275px"/>',
            self.cover,
        )

    # 增加阅读数
    def viewed(self):
        self.read_count += 1
        self.save(update_fields=['read_count'])

    cover_data.short_description = '文章封面'
    cover_admin.short_description = '文章封面'

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        db_table = "article"

    def __str__(self):
        return self.title
