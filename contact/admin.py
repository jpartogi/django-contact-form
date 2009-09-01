# $Id: admin.py b225c5739f6e 2009/09/01 11:18:01 jpartogi $

from django.contrib import admin

from contact.models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'department']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'sender_email','created']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Message, MessageAdmin)