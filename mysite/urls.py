from coderedcms import admin_urls as crx_admin_urls
from coderedcms import search_urls as crx_search_urls
from coderedcms import urls as crx_urls
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls
from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(crx_admin_urls)),
    path("docs/", include(wagtaildocs_urls)),
]

urlpatterns += i18n_patterns(
    path("search/", include(crx_search_urls)),
    path("search/", search_views.search, name="search"),
    path("", include(crx_urls)),
    path("", include(wagtail_urls)),
    # Add other URL configurations that require i18n here
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
