from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = patterns('',
#     # ... the rest of your URLconf goes here ...
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.home_page', name='home'),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
