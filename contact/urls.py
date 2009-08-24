from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'contact.views.form'),
)
