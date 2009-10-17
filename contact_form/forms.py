# $Id: forms.py ef5633b6df44 2009/09/06 14:08:22 jpartogi $

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