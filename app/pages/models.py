from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _

from content_editor.models import Region, Template, create_plugin_base

from feincms3.apps import AppsMixin
from feincms3.mixins import TemplateMixin, MenuMixin, LanguageMixin
from feincms3.pages import AbstractPage
from feincms3.plugins import image, richtext


class Page(
    AbstractPage,
    AppsMixin,      # For adding the articles app to pages through the CMS.
    TemplateMixin,  # Two page templates, one with only a main
                    # region and another with a sidebar as well.
    MenuMixin,      # We have a main and a footer navigation (meta).
    LanguageMixin,  # We're building a multilingual CMS. (Also,
                    # feincms3.apps depends on LanguageMixin
                    # currently.)
):

    # TemplateMixin
    TEMPLATES = [
        Template(
            key='standard',
            title=_('standard'),
            template_name='pages/standard.html',
            regions=(
                Region(key='main', title=_('Main')),
            ),
        ),
        Template(
            key='with-sidebar',
            title=_('with sidebar'),
            template_name='pages/with-sidebar.html',
            regions=(
                Region(key='main', title=_('Main')),
                Region(key='sidebar', title=_('Sidebar')),
            ),
        ),
    ]

    # MenuMixin
    MENUS = [
        ('main', _('main')),
        ('footer', _('footer')),
    ]

    # AppsMixin. We have two apps, one is for company PR, the other
    # for a more informal blog.
    #
    # NOTE! The app names (first element in the tuple) have to match the
    # article categories exactly for URL reversing and filtering articles by
    # app to work! (See app.articles.models.Article.CATEGORIES)
    APPLICATIONS = [
        ('publications', _('publications'), {
            'urlconf': 'app.articles.urls',
        }),
        ('blog', _('blog'), {
            'urlconf': 'app.articles.urls',
        }),
    ]


PagePlugin = create_plugin_base(Page)


class RichText(richtext.RichText, PagePlugin):
    pass


class Image(image.Image, PagePlugin):
    caption = models.CharField(
        _('caption'),
        max_length=200,
        blank=True,
    )
