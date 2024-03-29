from content_editor.admin import ContentEditor
from django.contrib import admin
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _
from feincms3.admin import TreeAdmin
from feincms3.plugins import image, richtext

from . import models


@admin.register(models.Page)
class PageAdmin(ContentEditor, TreeAdmin):
    list_display = [
        "indented_title",
        "move_column",
        "is_active",
        "menu",
        "language_code",
        "page_type",
    ]
    list_filter = ["is_active", "menu"]
    list_editable = ["is_active"]
    list_display_links = ["indented_title"]
    prepopulated_fields = {
        "slug": ("title",),
    }
    radio_fields = {
        "menu": admin.HORIZONTAL,
        "language_code": admin.HORIZONTAL,
        "page_type": admin.HORIZONTAL,
    }
    raw_id_fields = ["parent"]

    mptt_level_indent = 30

    fieldsets = [
        (
            None,
            {
                "fields": (
                    "is_active",
                    "title",
                    "parent",
                )
            },
        ),
        (
            capfirst(_("path")),
            {
                "fields": (
                    "slug",
                    "static_path",
                    "path",
                ),
                "classes": ("tabbed",),
            },
        ),
        (
            capfirst(_("settings")),
            {
                "fields": (
                    "menu",
                    "language_code",
                    "page_type",
                ),
                "classes": ("tabbed",),
            },
        ),
    ]

    inlines = [
        richtext.RichTextInline.create(model=models.RichText),
        image.ImageInline.create(model=models.Image),
    ]
