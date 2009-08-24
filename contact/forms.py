from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', widget=forms.TextInput())
    email = forms.EmailField(label='Your e-mail',widget=forms.TextInput())
    subject = forms.CharField(widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())