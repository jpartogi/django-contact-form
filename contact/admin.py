# $Id: admin.py e8fd065c6a51 2009/09/06 13:36:31 jpartogi $

from django.contrib import admin
from django.core import urlresolvers
from django.utils.translation import ugettext as _

from contact.models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department_url')

    def department_url(self, obj):
        change_url = urlresolvers.reverse('admin:contact_department_change', args=(obj.department.id,))
        return '<a href="%s">%s</a>' % (change_url, obj.department.name)
    department_url.allow_tags = True
    department_url.short_description = _('department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'created')

    def sender(self, obj):
        return '<a href="mailto:%s">%s</a>' % (obj.sender_email, obj.sender_name)
    sender.allow_tags = True
    sender.short_description = 'sender'

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Message, MessageAdmin)