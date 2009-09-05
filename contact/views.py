# $Id: views.py 22499ef140b8 2009/09/05 12:08:01 jpartogi $
from django.core.mail import send_mail
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect

from contact.forms import ContactForm

try:
    from recaptcha.client import captcha
except:
    raise ImproperlyConfigured("The recaptcha client library needs to be installed")

def form(request):

    try:
        recaptcha_pub_key = getattr(settings, 'RECAPTCHA_PUB_KEY')

        html_captcha = captcha.displayhtml(recaptcha_pub_key)
    except:
        raise ImproperlyConfigured("RECAPTCHA_PUB_KEY must be defined in the project's settings")

    try:
        recaptcha_private_key = getattr(settings, 'RECAPTCHA_PRIVATE_KEY')
    except:
        raise ImproperlyConfigured("RECAPTCHA_PRIVATE_KEY must be defined in project's settings")

    if request.method == 'POST':
        check_captcha = captcha.submit(request.POST['recaptcha_challenge_field'],
                            request.POST['recaptcha_response_field'],
                            recaptcha_private_key,
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