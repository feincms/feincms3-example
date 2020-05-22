from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    name = 'app.articles'
    verbose_name = capfirst(_('articles'))
