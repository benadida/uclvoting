from django.conf.urls.defaults import *

from views import index


urlpatterns = patterns('',
    (r'^$', index),
    
    # static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'})
)
