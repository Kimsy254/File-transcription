from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Worker,Client

from .models import User
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Worker)
admin.site.register(Client)