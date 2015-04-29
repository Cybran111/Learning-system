from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', "courses.assignments.views.assignments_view", name='assignments'),
                       # url(r'^(?P<username>\S+)/$', views.accounts, name='accounts'),

)