# $Id: admin.py 93f593ed4160 2009/09/06 12:10:32 jpartogi $

from django.contrib import admin

from contact.models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email','created')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Message, MessageAdmin)