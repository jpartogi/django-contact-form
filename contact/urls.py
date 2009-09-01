from django.conf.urls.defaults import *

import contact.views

urlpatterns = patterns('',
    url(r'^$', contact.views.form, name='contact-form'),
)
