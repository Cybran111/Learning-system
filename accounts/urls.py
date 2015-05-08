from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Learning_system.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^$', 'courses.views.home_page', name='home'),

                       # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'dashboard/login.html'},
                           name="login"),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {"next_page": "/"}, name="logout"),
                       url(r'^enroll/$', views.enroll, name='enroll'),
                       url(r'^profile/$', views.profile, name='profile'),
                       )

