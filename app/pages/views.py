from django.shortcuts import get_object_or_404, render

from .models import Page
from .renderer import renderer


def page_detail(request, path=None):
    page = get_object_or_404(
        Page.objects.active(),
        path=f"/{path}/" if path else "/",
    )
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
