# $Id: views.py 22499ef140b8 2009/09/05 12:08:01 jpartogi $
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib import messages

from .forms import ContactForm
from .models import EmailError

def form(request):
    contact = None
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                contact = form.save()
            except EmailError:
                messages.error(_('Verify your info, may be your email is wrong'))
            else:
            # TODO: Externalize this? Is i18n good enough?
                message = _("Thank you for contacting us. We'll get back to you shortly.")
                messages.success(request, message)
    else:
        form = ContactForm()

    return render_to_response('contact_form/form.html', {
        'form': form,
        'request' : request,
        'message' : contact,
    }, context_instance=RequestContext(request))
