from django.conf.urls import patterns, url, include
from . import views

__author__ = 'cybran'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'E_Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', 'courses.views.home_page', name='home'),

                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r'^register/$', views.register, name='register'),
# url(r'^admin/', include(admin.site.urls)),
)