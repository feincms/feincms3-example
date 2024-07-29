from django.shortcuts import render
from feincms3.root.middleware import create_page_if_404_middleware

from .models import Page
from .renderer import renderer


def handler(request, page):
    page.activate_language(request)
    return render(
        request,
        page.type.template_name,
        {
            "page": page,
            "regions": renderer.regions_from_item(
                page,
                inherit_from=page.ancestors().reverse(),
                timeout=10,
            ),
        },
    )


page_if_404_middleware = create_page_if_404_middleware(
    queryset=lambda request: Page.objects.active(), handler=handler, language_code_redirect=True
)
