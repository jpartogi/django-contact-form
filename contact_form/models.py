# $Id: models.py ef5633b6df44 2009/09/06 14:08:22 jpartogi $

from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage, BadHeaderError
from django.conf import settings

from smtplib import SMTPException

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/department/%s" % ( self.id )


class Subject(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    sender_name = models.CharField(max_length=50, verbose_name= _('sender name'))
    sender_email = models.EmailField(verbose_name= _('sender e-mail'))
    subject = models.ForeignKey(Subject, verbose_name= _('subject'), blank=True,
                               null=True)
    other_subject = models.CharField(_('other subject'), max_length=100, blank=True)
    content = models.TextField(verbose_name= _('message'))
    created = models.DateTimeField(auto_now_add=True, verbose_name= _('sent'))
    is_spam = models.BooleanField(_('is spam'), default=False)

    def __unicode__(self):
        return ' | '.join((self.subject.title, self.sender_name, self.sender_email))

class EmailError(Exception):
    pass

@receiver(post_save, sender=Message)
def send_contact_mail(sender, **kwargs):
    message =  kwargs['instance']
    if message.is_spam:
        return
    subject = " ".join((message.subject.title, message.other_subject))

    # message to the sender
    email = EmailMessage(_("Copy: %s")%subject,
                         _("Thank you for contacting us. We'll get back to you shortly."),
                         settings.DEFAULT_FROM_EMAIL,
                         (message.sender_email,),
                         headers = {'Reply-To':
                                    message.subject.department.email,})
    try:
        email.send(False)
    except (BadHeaderError, SMTPException), e:
        raise EmailError

    # message to the department
    email = EmailMessage(_("Contact form: %s")%subject,
                         message.content,
                         settings.DEFAULT_FROM_EMAIL,
                         (message.subject.department.email,),
                         headers = {'Reply-To': message.sender_email})

    try:
        email.send(False)
    except (BadHeaderError, SMTPException), e:
        raise EmailError

