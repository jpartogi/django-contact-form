# $Id: forms.py ef5633b6df44 2009/09/06 14:08:22 jpartogi $
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from contact_form.models import Message, Subject

# Override the labels
class ContactForm(ModelForm):
    sender_name = forms.CharField(label=_('Your name'), widget=forms.TextInput())
    sender_email = forms.EmailField(label=_('Your e-mail'), widget=forms.TextInput())

    # This fields is for spam protection
    # Invisible Captcha and it has to be hidden via css
    tricky = forms.CharField(label=_('other1'), widget=forms.TextInput(),
                             required=False)
    # Needed here if we want to set to True if tricky is answered
    is_spam = forms.BooleanField(label=_('are you a robot?'), required=False)

    class Meta:
        model = Message

    class Media:
        # this media is needed for hiding the invisible Captcha from
        # human users
        js = ('media/js/tricky_field.js',)
        css = {'all': ('media/css/tricky_field.css',),}

    def clean(self):
        cleaned_data = self.cleaned_data
        # if is empty is not spam
        tricky = cleaned_data.get('tricky')
        if tricky:
            cleaned_data['is_spam'] = True

        if not cleaned_data.get('subject'):
            try:
                subject = Subject.objects.get(department__name=_('other'))
            except Subject.DoesNotExist, e:
                message = _('No "other" Departement is in the DataBase :%s')%e.message
                e.args =  (message,)
                raise e

            cleaned_data['subject'] = subject

        return cleaned_data
