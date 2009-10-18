# $Id: forms.py ef5633b6df44 2009/09/06 14:08:22 jpartogi $
from django.core.mail import send_mail
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from contact_form.models import Message

# Override the labels
class ContactForm(ModelForm):
    sender_name = forms.CharField(label=_('Your name'), widget=forms.TextInput())
    sender_email = forms.EmailField(label=_('Your e-mail'), widget=forms.TextInput())

    class Meta:
        model = Message

    def save(self, commit=True):
        super(ContactForm, self).save(commit)
        
        contact = self.instance
        
        send_mail(contact.subject.title, contact.message,
            contact.sender_name +'<' + contact.sender_email + '>',
            [contact.subject.department.email], fail_silently=False)