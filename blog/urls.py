from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.viwes import home_page,reg
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'$^',home_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/$',reg),
    url(r'^registration/thanks/$',home_page)
)

urlpatterns+=staticfiles_urlpatterns()