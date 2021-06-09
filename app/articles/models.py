from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from feincms3.applications import reverse_app
from feincms3.inline_ckeditor import InlineCKEditorField
from feincms3.plugins import image


class ArticleManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def published(self):
        return self.filter(
            is_active=True,
            publication_date__lte=timezone.now(),
        )


class Article(models.Model):
    """
    The articles models. We're using the ``InlineCKEditorField`` field
    which provides us with an inline CKEditor instance and HTML-sanitizer's
    post-processing. This code snippet also contains the trickiest bit of this
    whole project, ``Article``'s ``get_absolute_url`` implementation.
    """

    # NOTE! All categories require a matching entry in
    # app.pages.models.Page.APPLICATIONS.
    CATEGORIES = (
        ("blog", _("blog")),
        ("publications", _("publications")),
    )

    is_active = models.BooleanField(_("is active"), default=False)
    title = models.CharField(_("title"), max_length=200)
    slug = models.SlugField(_("slug"), unique_for_year="publication_date")
    publication_date = models.DateTimeField(_("publication date"), default=timezone.now)
    body = InlineCKEditorField(_("body"))
    category = models.CharField(
        _("category"),
        max_length=20,
        db_index=True,
        choices=CATEGORIES,
    )

    objects = ArticleManager()

    class Meta:
        get_latest_by = "publication_date"
        ordering = ["-publication_date"]
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        This is the trickiest bit of this whole project.
        reverse_app is a simple wrapper around
        feincms3.applications.reverse_any, which is exactly the same as
        django.core.urlresolvers.reverse with the small difference
        that it accepts a list of viewnames and returns the first
        result where no NoReverseMatch exception is raised.

        The viewnames tried in sequence by reverse_app are
        (assuming that the project is configured with german,
        english and french as available languages, and french as
        active language, and assuming that the current article is
        a publication):

        - fr.publications.article-detail
        - fr.articles.article-detail
        - de.publications.article-detail
        - de.articles.article-detail
        - en.publications.article-detail
        - en.articles.article-detail
        - Otherwise, let the NoReverseMatch exception bubble.

        reverse_app tries harder returning an URL in the correct
        language than returning an URL for the correct app. Better
        show a PR publication on the blog page than switching
        languages.
        """

        return reverse_app(
            (self.category, "articles"),
            "article-detail",
            kwargs={
                "year": self.publication_date.year,
                "slug": self.slug,
            },
        )


class Image(image.Image):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name=_("article"),
        related_name="images",
    )
    caption = models.CharField(
        _("caption"),
        max_length=200,
        blank=True,
    )
