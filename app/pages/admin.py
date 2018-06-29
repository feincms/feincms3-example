from __future__ import unicode_literals

from django.contrib import admin
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from content_editor.admin import ContentEditor
from feincms3 import plugins
from feincms3.admin import TreeAdmin
from js_asset import JS

from . import models


@admin.register(models.Page)
class PageAdmin(ContentEditor, TreeAdmin):
    list_display = [
        'indented_title', 'move_column',
        'is_active', 'menu',
        'language_code',
        'template_key',
        'application',
    ]
    list_filter = ['is_active', 'menu']
    list_editable = ['is_active']
    list_display_links = ['indented_title']
    prepopulated_fields = {
        'slug': ('title',),
    }
    radio_fields = {
        'menu': admin.HORIZONTAL,
        'language_code': admin.HORIZONTAL,
        'template_key': admin.HORIZONTAL,
        'application': admin.HORIZONTAL,
    }
    raw_id_fields = ['parent']

    mptt_level_indent = 30

    fieldsets = [
        (None, {
            'fields': (
                'is_active',
                'title',
                'parent',
            )
        }),
        (capfirst(_('path')), {
            'fields': (
                'slug',
                'static_path',
                'path',
            ),
            'classes': ('tabbed',),
        }),
        (capfirst(_('settings')), {
            'fields': (
                'menu',
                'language_code',
                'template_key',
                'application',
            ),
            'classes': ('tabbed',),
        }),
    ]

    inlines = [
        plugins.RichTextInline.create(model=models.RichText),
        plugins.ImageInline.create(model=models.Image),
    ]

    class Media:
        js = (
            JS('https://use.fontawesome.com/releases/v5.0.10/js/all.js', {
                'async': 'async',
                'integrity': 'sha384-slN8GvtUJGnv6ca26v8EzVaR9DC58QEwsIk9q1QXdCU8Yu8ck/tL/5szYlBbqmS+',  # noqa
                'crossorigin': 'anonymous',
            }, static=False),
            'app/plugin_buttons.js',
        )
