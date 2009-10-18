# $Id: views.py 22499ef140b8 2009/09/05 12:08:01 jpartogi $
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from contact_form.forms import ContactForm

def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            request.notifications.create(_('The message has been sent successfully'), 'success')
    else:
        form = ContactForm()

    return render_to_response('contact/form.html', {
        'form': form,
        'request' : request,
    }, context_instance=RequestContext(request))