# $Id: views.py 22499ef140b8 2009/09/05 12:08:01 jpartogi $
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext

from contact_form.forms import ContactForm

def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            send_mail(contact.subject.title, contact.message,
                    contact.sender_name +'<' + contact.sender_email + '>',
                    [contact.subject.department.email], fail_silently=False)

            request.notifications.create(_('The message has been sent successfully'), 'success')

    else:
        form = ContactForm()

    return render_to_response('contact/form.html', {
        'form': form,
        'request' : request,
    }, context_instance=RequestContext(request))