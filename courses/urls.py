from django.conf.urls import patterns, url, include

__author__ = 'cybran'

# TODO: ugly pattern names
manage_urlpatterns = patterns('courses.views', url(r'^$', "manage_course_view", name='manage'),
                              url(r'^week/$', "manage_week_view", name='manage_week'),
                              url(r'^week/(?P<week_number>\d+)/$', "manage_lecture_view", name='manage_lecture'), )

urlpatterns = patterns('courses.views', url(r'^new$', "create_course_view", name='new_course'),
                       url(r'^(?P<course_id>\d+)/$', "course_view", name='course_page'),
                       url(r'^(?P<course_id>\d+)/lectures/$', "lecture_list_view", name='lectures'),
                       url(r"^(?P<course_id>\d+)/week/(?P<week_number>\d+)/lecture/(?P<lecture_number>\d+)/$",
                           "lecture_view", name="lecture"),
                       url(r'^(?P<course_id>\d+)/manage/', include(manage_urlpatterns)))
