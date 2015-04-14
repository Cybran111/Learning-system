from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'E_Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', 'courses.views.home_page', name='home'),

                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.auth, name='login'),
                       url(r'^enroll/$', views.enroll, name='enroll'),
                       url(r'^(?P<username>\S+)/$', views.dashboard, name='dashboard'),

)

