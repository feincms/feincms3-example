from django.shortcuts import get_object_or_404, render
from feincms3.regions import Regions

from .models import Page
from .renderer import renderer


def page_detail(request, path=None):
    page = get_object_or_404(
        Page.objects.active(),
        path="/{}/".format(path) if path else "/",
    )
    page.activate_language(request)
    return render(
        request,
        page.type.template_name,
        {
            "page": page,
            "regions": Regions.from_item(
                page, renderer=renderer, inherit_from=page.ancestors().reverse()
            ),
        },
    )
