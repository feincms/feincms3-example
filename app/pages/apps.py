from django.apps import AppConfig
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _


class PagesConfig(AppConfig):
    name = "app.pages"
    verbose_name = capfirst(_("pages"))
