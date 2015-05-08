from django.conf.urls import patterns, url, include

__author__ = 'cybran'

urlpatterns = patterns('courses.views',
                       url(r'^(?P<course_id>\d+)/$', "course_dashboard_view", name='course_dashboard'),
                       url(r'^(?P<course_id>\d+)/overview/$', "course_overview_view", name='course_overview'),
                       url(r'^(?P<course_id>\d+)/lectures/$', "lecture_list_view", name='lectures'),
                       url(r"^(?P<course_id>\d+)/week/(?P<week_number>\d+)/lecture/(?P<lecture_number>\d+)/$",
                           "lecture_view", name="lecture"),
                       url(r'^(?P<course_id>\d+)/news/$', "news_view", name='news'),

                       url(r'^(?P<course_id>\d+)/assignments/',
                           include('courses.assignments.urls', namespace='assignments')),
                       url(r'^(?P<course_id>\d+)/assessments/',
                           include('courses.assessments.urls', namespace='assessments')),
)
