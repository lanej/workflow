"""
URL routing patterns for the Deis project.

This is the "master" urls.py which then includes the urls.py files of
installed apps.
"""

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.views import HealthCheckView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^health-check$', HealthCheckView.as_view()),
    url(r'^v2/', include('api.urls')),
)

if settings.WEB_ENABLED:
    urlpatterns += patterns(
        '',
        url(r'^', include('web.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
