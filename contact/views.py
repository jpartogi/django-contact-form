from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext

from contact.forms import ContactForm

def form(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
	    to_email = form.cleaned_data['to_email']

            send_mail(subject, message,
                    name +'<' + email + '>', [to_email], fail_silently=False)

    else:
        form = ContactForm()

    return render_to_response('contact/form.html', {'form': form,
                                                    'request' : request},
                context_instance=RequestContext(request))
