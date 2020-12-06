from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    bio = models.CharField(
        max_length=240,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        )
    )
    birth_date = models.DateField(null=True, blank=True)
    user_type = models.CharField(
        max_length=240,
        choices= (
            ('Organization', 'Organization'),
            ('Individual', 'Individual')
        ),
        default='Individual'
    )
    especiality_area = models.CharField(
        max_length=240,
        null= True,
        choices= (
            ('Web Development', 'Web Development'),
            ('Design', 'Design'),
            ('Sales', 'Sales')
        )
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.email}"