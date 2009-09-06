# $Id: models.py 324bfbdd83ad 2009/09/06 13:23:11 jpartogi $

from django.db import models
from django.utils.translation import ugettext as _

class Department(models.Model):
    name = models.CharField(max_length=50)
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
    sender_name = models.CharField(max_length=50, verbose_name= _('your name'))
    sender_email = models.EmailField(verbose_name= _('your e-mail'))
    subject = models.ForeignKey(Subject, verbose_name= _('subject'))
    message = models.TextField(verbose_name= _('message'))
    created = models.DateTimeField(auto_now_add=True, verbose_name= _('sent'))