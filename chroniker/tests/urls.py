try:
    # Removed in Django 1.6
    from django.conf.urls.defaults import include
    from django.conf.urls.defaults import url as re_path
except ImportError:
    try:
        from django.conf.urls import include
        from django.conf.urls import url as re_path
    except ImportError:
        from django.urls import re_path

try:
    # Relocated in Django 1.6
    from django.conf.urls.defaults import patterns
except ImportError:
    # Completely removed in Django 1.10
    try:
        from django.conf.urls import patterns
    except ImportError:
        patterns = None

from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

admin.autodiscover()

try:
    _patterns = [
        re_path(r"^admin/", include(admin.site.urls)),
    ]
except ImproperlyConfigured:
    # Django >= 2.1.7.
    _patterns = [
        re_path(r"^admin/", admin.site.urls),
    ]

if patterns is None:
    urlpatterns = _patterns
else:
    urlpatterns = patterns("", *_patterns)
