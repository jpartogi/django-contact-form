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
            # TODO: Externalize this? Is i18n good enough?
            message = "Thank you for contacting us. We'll get back to you shortly."
            request.notifications.create(_(message),
                'success')
    else:
        form = ContactForm()

    return render_to_response('contact_form/form.html', {
        'form': form,
        'request' : request,
    }, context_instance=RequestContext(request))