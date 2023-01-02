"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


#  AbstractBaseUser - functionality for authentication in the system
#  PermissionsMixin - functionality for the permissions and fields


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class JobListing(models.Model):
    """'''Job listing object.'''"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_seniority = models.CharField(max_length=255)
    job_description = models.TextField(blank=True)
    salary_max = models.IntegerField(default=5000, blank=True, null=True)
    salary_min = models.IntegerField(default=4000, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.job_title
