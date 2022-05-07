"""Django_Hexo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 主页
    path('', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),

    # 分类统计
    path(r'category/', views.CategoryList.as_view(), name='category_list'),

    # 文章分类
    re_path(r'category/cg(?P<pk>\d+)', views.CategoryView.as_view(), name='article_category'),

    # 标签统计
    path(r'tag/', views.TagList.as_view(), name='tag_list'),

    # 文章标签
    re_path(r'tag/tg(?P<pk>\d+)', views.TagView.as_view(), name='article_tag'),

    # 文章归档
    path('article/', views.Archive.as_view(), name='archive'),

    # 关于本站
    path('about/', views.About.as_view(),name='about')

] + static(settings.STATIC_URL)
