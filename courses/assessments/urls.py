from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', "courses.assessments.views.assessments_view", name='assessments'),
                       url(r'^week/(?P<week_id>\S+)/assessments/(?P<assessment_id>\S+)/overview/$',
                           "courses.assessments.views.assessment_overview", name='overview'),

                       url(r'^week/(?P<week_id>\S+)/assessments/(?P<assessment_id>\S+)/attempt/$',
                           "courses.assessments.views.assessment_attempt", name='attempt'),

                       # url(r'^feedback/(?P<feedback_route>\S+)/$', "courses.assignments.views.feedback_view",
                       #     name='feedback'),

)