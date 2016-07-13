
from django.conf.urls import patterns, include, url
from views import AddContent
from views import AddQuestion
from views import Output

urlpatterns = patterns('',

    url(r'^/add$', AddContent.as_view()),
    url(r'^/update/(?P<id>[1-9][0-9]*)$',AddContent.as_view()),
    url(r'^/delete/(?P<pk>[0-9]+)$',AddContent.as_view()),  
    url(r'^/addq$', AddQuestion.as_view()),
    url(r'^/postq/(?P<subject>[A-z][A-z]*)$',AddQuestion.as_view()),
    url(r'^/output/(?P<subject>[A-z]*)/(?P<difficulty>[A-z]*)$',Output.as_view()),
#  url(r'^/update',Content.as_view()),
)


