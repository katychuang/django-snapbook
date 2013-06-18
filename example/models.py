from datetime           import timedelta
from django.db          import models


class Style(models.Model):
    font        = models.CharField(max_length=30)
    section     = models.CharField(max_length=30)
