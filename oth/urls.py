from django.conf.urls import patterns, include, url
from player.views import index,authorize,log_out
from level.views import level_view,check_answer,level_file,level_scrape
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from oth import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index),
	url(r'^authorize/$',authorize),
	url(r'^logout/$',log_out),
	url(r'^numbers/$',level_scrape),
	url(r'^level/(?P<slug>\w+)/$',level_view),
	url(r'^level/(?P<filename>[.\w]+)/$',level_file),
	url(r'^check_answer/$',check_answer),
	url(r'^fandjango/', include('fandjango.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT})
)


#urlpatterns += staticfiles_urlpatterns()
