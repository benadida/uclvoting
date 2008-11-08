from django.conf.urls.defaults import *

from views import index, vote, election, voter, submit_vote


urlpatterns = patterns('',
    (r'^$', index),
    (r'^vote$', vote),
    (r'^election$', election),
    (r'^election/voter/(?P<voter_id>[^/]*)$', voter),
    (r'^election/submit_vote$', submit_vote),
    
    # static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'})
)
