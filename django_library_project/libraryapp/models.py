from django.db.models import CharField, EmailField, DateTimeField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, password=None, **other_fields):
        if not email:
            raise ValueError('You must provide an email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_admin') is not True:
            raise ValueError('Superuser must be assigned to is_admin=True.')

        user = self.create_user(email=email, user_name=user_name, password=password, **other_fields)
        user.save()
        return user


class UserManager(AbstractBaseUser, PermissionsMixin):
    email: EmailField = models.EmailField(unique=True, max_length=255)
    user_name: CharField = models.CharField(unique=True, max_length=150)
    registration_date: DateTimeField = models.DateTimeField("Registration Date", auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects: CustomUserManager = CustomUserManager()

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return f"{self.email} {self.user_name} {self.registration_date} {self.is_staff} {self.is_admin} {self.is_active}"

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    # """Is the user a member of staff?"""
    # Simplest possible answer: All admins are staff
    # return self.is_admin


class User(models.Model):
    first_name: CharField = models.CharField("First Name", max_length=240)
    last_name: CharField = models.CharField("Last Name", max_length=240)
    email: EmailField = models.EmailField()
    phone: CharField = models.CharField("Phone Number", max_length=12)
    password: CharField = models.CharField(max_length=128)
    registration_date: DateTimeField = models.DateTimeField("Registration Date", auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone} {self.registration_date}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
