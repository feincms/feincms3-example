from django.http import HttpResponseRedirect
from django.urls import re_path

from app.pages import views

app_name = "pages"
urlpatterns = [
    re_path(
        r"^$",
        lambda request: HttpResponseRedirect("/%s/" % request.LANGUAGE_CODE),
    ),
    re_path(
        r"^(?P<path>[-\w/]+)/$",
        views.page_detail,
        name="page",
    ),
    re_path(
        r"^$",
        views.page_detail,
        name="root",
    ),
]
