from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'E_Learning_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'course.views.home_page', name='home'),
    url(r'^courses/', include('course.urls', namespace='courses')),
    # url(r'^admin/', include(admin.site.urls)),
)
