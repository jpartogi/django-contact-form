from django.conf.urls.defaults import *

urlpatterns = patterns('contact.views',
    (r'^$', 'form'),
)
