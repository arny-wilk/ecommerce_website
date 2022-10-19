from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import Textarea
from django.db import models

# Register your models here.
from .models import UserManager

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserManager
        fields = ('email', 'user_name')

    def clean_password2(self):
        # Check that the two password entries math
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserManager
        fields = ('email', 'user_name', 'password', 'is_active', 'is_admin')


class UserAdminConfig(BaseUserAdmin):
    # The forms to add  and change user instances
    form = UserChangeForm
    add_form = UserCreationForm


    # The fields to be used in displaying the User model
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User
    list_display = ('email', 'user_name', 'registration_date', 'is_staff', 'is_admin', 'is_active')
    list_filter = ('email', 'user_name', 'is_staff', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }

    # add fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('UserManager',),
            'fields': ('email', 'user_name', 'password', 'is_staff', 'is_admin', 'is_active')
        }
         ),
    )
    search_fields = ('email', 'user_name')
    ordering = ('registration_date',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(UserManager, UserAdminConfig)
