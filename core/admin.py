from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Family

admin.site.register(MyUser, UserAdmin)
admin.site.register(Family)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('name', 'family')}),
