from content_editor.models import Region, create_plugin_base
from django.db import models
from django.utils.translation import gettext_lazy as _
from feincms3.applications import ApplicationType, PageTypeMixin, TemplateType
from feincms3.mixins import LanguageMixin, MenuMixin
from feincms3.pages import AbstractPage
from feincms3.plugins import image, richtext


class Page(
    AbstractPage,
    PageTypeMixin,  # For adding the articles app to pages through the CMS.
    MenuMixin,  # We have a main and a footer navigation (meta).
    LanguageMixin,  # We're building a multilingual CMS. (Also,
    # feincms3.applications depends on LanguageMixin
    # currently.)
):
    TYPES = [
        TemplateType(
            key="standard",
            title=_("standard"),
            template_name="pages/standard.html",
            regions=(Region(key="main", title=_("Main")),),
        ),
        TemplateType(
            key="with-sidebar",
            title=_("with sidebar"),
            template_name="pages/with-sidebar.html",
            regions=(
                Region(key="main", title=_("Main")),
                Region(key="sidebar", title=_("Sidebar")),
            ),
        ),
        ApplicationType(
            key="publications",
            title=_("publications"),
            urlconf="app.articles.urls",
            regions=(Region(key="main", title=_("Main")),),
        ),
        ApplicationType(
            key="blog",
            title=_("blog"),
            urlconf="app.articles.urls",
            regions=(Region(key="main", title=_("Main")),),
        ),
    ]

    # MenuMixin
    MENUS = [
        ("main", _("main")),
        ("footer", _("footer")),
    ]


PagePlugin = create_plugin_base(Page)


class RichText(richtext.RichText, PagePlugin):
    pass


class Image(image.Image, PagePlugin):
    caption = models.CharField(
        _("caption"),
        max_length=200,
        blank=True,
    )
