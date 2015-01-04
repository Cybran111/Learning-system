from django.conf.urls import patterns, url

from courses import views


__author__ = 'cybran'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'E_Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', 'courses.views.home_page', name='home'),

                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<course_id>\d+)/$', views.course_view, name='course_page'),

                       url(r'^(?P<course_id>\d+)/lectures/$', views.lectures_view, name='course_lectures'),

                       url(r'^(?P<course_id>\d+)/manage/$', views.manage_course_view, name='manage_course'),
                       url(r'^(?P<course_id>\d+)/manage/week/$', views.manage_week_view, name='manage_week'),
                       url(r'^(?P<course_id>\d+)/manage/week/(?P<week_number>\d+)/$', views.manage_lecture_view,
                           name='manage_lecture'),

                       url(r'^new$', views.create_course_view, name='new_course'),

                       # url(r'^admin/', include(admin.site.urls)),
)



