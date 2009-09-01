# $Id: models.py b225c5739f6e 2009/09/01 11:18:01 jpartogi $

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

class Message(models.Model):
    sender_name = models.CharField(max_length=50, verbose_name='Your Name')
    sender_email = models.EmailField(verbose_name='Your E-mail')
    subject = models.ForeignKey(Subject)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)