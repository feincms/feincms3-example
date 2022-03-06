from django.urls import re_path

from app.articles import views


app_name = "articles"
ignore_app_name_mismatch = True  # It's expected
urlpatterns = [
    re_path(
        r"^$",
        views.article_list,
        name="article-list",
    ),
    re_path(
        r"^(?P<year>\d{4})/(?P<slug>[-\w]+)/$",
        views.article_detail,
        name="article-detail",
    ),
]
