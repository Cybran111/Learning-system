from django.conf.urls import patterns, url

from courses import views


__author__ = 'cybran'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'E_Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', 'courses.views.home_page', name='home'),

                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r'(?P<course_id>\d+)/$', views.course_view, name='course_page'),
                       url(r'^new$', views.create_course, name='new_course'),

                       # url(r'^admin/', include(admin.site.urls)),
)