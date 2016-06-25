from __future__ import unicode_literals

from django.conf.urls import url

from app.articles import views


app_name = 'articles'
urlpatterns = [
    url(
        r'^$',
        views.article_list,
        name='article-list',
    ),
    url(
        r'^(?P<year>\d{4})/(?P<slug>[-\w]+)/$',
        views.article_detail,
        name='article-detail',
    ),
]
