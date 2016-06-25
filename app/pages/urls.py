from __future__ import unicode_literals

from django.conf.urls import url
from django.http import HttpResponseRedirect

from app.pages import views


app_name = 'pages'
urlpatterns = [
    url(
        r'^$',
        lambda request: HttpResponseRedirect('/%s/' % request.LANGUAGE_CODE),
    ),
    url(
        r'^(?P<path>[-\w/]+)/$',
        views.page_detail,
        name='page',
    ),
    url(
        r'^$',
        views.page_detail,
        name='root',
    ),
]
