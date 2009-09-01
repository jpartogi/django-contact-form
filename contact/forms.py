# $Id: forms.py b225c5739f6e 2009/09/01 11:18:01 jpartogi $

from django import forms
from django.forms import ModelForm

from contact.models import Message

class ContactForm(ModelForm):
    #name = forms.CharField(label='Your name', widget=forms.TextInput())
    #email = forms.EmailField(label='Your e-mail',widget=forms.TextInput())
    #subject = forms.CharField(widget=forms.TextInput())
    #message = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Message