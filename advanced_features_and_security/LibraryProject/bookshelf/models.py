from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password, **extra_fields):
        if not email:
            raise ValueError('Email Field Must be set')
        if not date_of_birth:
            raise ValueError('Date of Birth Field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth)
        user.set_password(password)

        return user

    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not date_of_birth:
            raise ValueError('Date of Birth is Required')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be staff')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be Superuse')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField()

    objects = CustomUserManager()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view', 'Can View'),
            ('can_create', 'Can Create'),
            ('can_edit', 'Can Edit'),
            ('can_delete', 'Can Delete'),
        ]