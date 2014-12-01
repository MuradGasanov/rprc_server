from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^django_admin/', include(admin.site.urls)),
                       url(r'^', include('main.urls')),
                       )
