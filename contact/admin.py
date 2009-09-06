# $Id: admin.py 324bfbdd83ad 2009/09/06 13:23:11 jpartogi $

from django.contrib import admin
from django.core import urlresolvers
from django.utils.translation import ugettext as _

from contact.models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department_url')

    def department_url(self, obj):
        change_url = urlresolvers.reverse('admin:contact_department_change', args=(obj.department.id,))
        return "<a href='%s'>%s</a>" % (change_url, obj.department.name)
    department_url.allow_tags = True
    department_url.short_description = _('department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email','created')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Message, MessageAdmin)