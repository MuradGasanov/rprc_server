__author__ = 'Murad'

from django.conf.urls import patterns, include, url
from main.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/$', log_in),
    url(r'^logout/$', log_out),
)