from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from blog import models as m_models


# Create your views here.


# 首页
class Home(View):
    def get(self, request):
        # 获取所有文章，按新增时间倒序
        all_articles = m_models.Article.objects.all().order_by('-pub_time')
        # 获取所有推荐的文章
        top_articles = m_models.Article.objects.filter(is_recommend=1)
        # 首页分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_articles, 9, request=request)
        articles = p.page(page)

        return render(request, 'home.html', {
            'all_articles': articles,
            'top_articles': top_articles,
        })
