from django.db import models
from mdeditor.fields import MDTextField
from datetime import datetime, date
from django.utils.html import format_html
import random


def get_default_category():
    return Category.objects.get_or_create(name='默认', slug='default')[0].pk


def generate_random_num(l: int, a: int, b: int):
    random.seed(datetime.now().strftime('%Y%m%d%H%M%S'))
    return str(random.randint(a, b)).zfill(l)


# Create your models here.

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='标签名称')
    slug = models.CharField(max_length=50, unique=True, default=generate_random_num(8, 0, 99999999),
                            verbose_name='标签英文名称')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    get_items.short_description = '文章数'

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        db_table = "tag"

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    slug = models.CharField(max_length=50, verbose_name='分类英文名称')
    # index = models.IntegerField(default=99, verbose_name='分类排序')
    active = models.BooleanField(default=False, verbose_name='是否添加到菜单')
    icon = models.CharField(max_length=30, default='fa-home', verbose_name='菜单图标')

    # 统计文章数 并放入后台
    def get_items(self):
        return len(self.article_set.all())

    def icon_data(self):
        return format_html(
            '<i class="{}"></i>',
            self.icon,
        )

    get_items.short_description = '文章数'
    icon_data.short_description = '图标预览'

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        db_table = "category"

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    summary = models.TextField(max_length=100, verbose_name='文章概述')
    cover = models.CharField(max_length=200, default='https://image.3001.net/images/20200304/15832956271308.jpg',
                             verbose_name='文章封面')
    content = MDTextField(verbose_name='文章内容')
    read_count = models.IntegerField(default=0, verbose_name='阅读次数')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    pub_time = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.SET_DEFAULT,
                                 default=get_default_category())
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    article_id = models.CharField(max_length=14,
                                  default=date.today().strftime("%Y%m%d") + generate_random_num(6, 0, 999999),
                                  verbose_name='文章编号', primary_key=True, editable=False)

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


