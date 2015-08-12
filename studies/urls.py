from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
