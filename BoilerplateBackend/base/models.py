from django.db import models

from ..core.models import CustomUser

import datetime

# Create your models here.
class Contest(models.Model):
    #Figure out how to deal with owners
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date_limit_participation = models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=datetime.date.today
        )
    date_end =  models.DateField(
        auto_now=False, 
        auto_now_add=False,
        default=datetime.date.today
        )
    owner = models.ForeignKey(
        'core.CustomUser', 
        related_name='Contest', 
        on_delete=models.CASCADE,
        null=True
    )
    participants = models.ForeignKey(
        "core.CustomUser",
        related_name='+',
        on_delete=models.CASCADE,
        null=True
        #Look into what related_name does
    )
    