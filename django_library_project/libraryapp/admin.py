from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models

# Register your models here.
from .models import UserManager


class UserAdminConfig(UserAdmin):
    model = UserManager
    search_fields = ('email', 'user_name')
    list_filter = ('email', 'user_name', 'is_staff', 'is_admin', 'is_active')
    ordering = ('registration_date',)
    list_display = ('email', 'user_name', 'registration_date', 'is_staff', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('UserManager',),
            'fields': ('email', 'user_name', 'password', 'is_staff', 'is_admin', 'is_active')
        }
         ),
    )


admin.site.register(UserManager, UserAdminConfig)
