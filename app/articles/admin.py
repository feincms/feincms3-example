from __future__ import unicode_literals

from django.contrib import admin

from . import models


class ImageInline(admin.TabularInline):
    model = models.Image
    extra = 0


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "publication_date"
    inlines = [ImageInline]
    list_display = ["title", "is_active", "publication_date", "category"]
    list_editable = ["is_active"]
    list_filter = ["is_active", "category"]
    prepopulated_fields = {
        "slug": ("title",),
    }
    radio_fields = {
        "category": admin.HORIZONTAL,
    }

    fieldsets = [
        (
            None,
            {
                "fields": (
                    ("is_active",),
                    ("title", "slug"),
                    "publication_date",
                    "category",
                    "body",
                )
            },
        ),
    ]
