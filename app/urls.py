from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,) + [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"", include("app.pages.urls")),
]
