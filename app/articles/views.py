from django.shortcuts import get_object_or_404
from feincms3.applications import page_for_app_request
from feincms3.shortcuts import render_detail, render_list

from .models import Article


def article_list(request):
    page = page_for_app_request(request)
    page.activate_language(request)
    return render_list(
        request,
        # Only show articles for the current app.
        Article.objects.published()
        .filter(
            category=page.application,
        )
        .prefetch_related("images"),
        {"page": page},
        paginate_by=10,
    )


def article_detail(request, year, slug):
    page = page_for_app_request(request)
    page.activate_language(request)
    return render_detail(
        request,
        # We are NOT filtering for the current app. If, for example, the
        # blog application is inactive, we'd rather show the article in
        # the publication app than not at all. Of course if this behavior
        # isn't a good fit for you, simply add ``category=page.application``
        # here.
        get_object_or_404(
            Article.objects.published(),
            publication_date__year=year,
            slug=slug,
        ),
        {"page": page},
    )
