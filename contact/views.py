# $Id: views.py b225c5739f6e 2009/09/01 11:18:01 jpartogi $
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect

from recaptcha.client import captcha

from contact.forms import ContactForm

def form(request):
    html_captcha = captcha.displayhtml(settings.RECAPTCHA_PUB_KEY)

    if request.method == 'POST':
        check_captcha = captcha.submit(request.POST['recaptcha_challenge_field'],
                            request.POST['recaptcha_response_field'],
                            settings.RECAPTCHA_PRIVATE_KEY,
                            request.META['SERVER_NAME'])
                            
        if check_captcha.is_valid is False:
            # Captcha is wrong show an error ...
            request.notifications.create('Captcha challenge is wrong.', 'error')

            return HttpResponseRedirect(request.path)

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            send_mail(contact.subject.title, contact.message,
                    contact.sender_name +'<' + contact.sender_email + '>',
                    [contact.subject.department.email], fail_silently=False)

            request.notifications.create('The message has been sent successfully.', 'success')

    else:
        form = ContactForm()

    return render_to_response('contact/form.html', {
        'form': form,
        'request' : request,
        'html_captcha': html_captcha,
    }, context_instance=RequestContext(request))
