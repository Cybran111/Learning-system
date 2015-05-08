from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', "courses.assignments.views.assignments_view", name='assignments'),
                       url(r'^week/(?P<week_id>\S+)/assignment/(?P<assignment_id>\S+)/$',
                           "courses.assignments.views.assignment_view", name='assignment'),

                       url(r'^feedback/(?P<feedback_route>\S+)/$', "courses.assignments.views.feedback_view",
                           name='feedback'),
                       )