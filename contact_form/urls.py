from django.conf.urls.defaults import *

import contact_form.views

urlpatterns = patterns('',
    url(r'^$', contact_form.views.form, name='contact-form'),
)
