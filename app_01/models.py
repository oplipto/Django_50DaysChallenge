from django.db import models
from django.utils import timezone

# Create your models here.

class app_types(models.Model):
    app_type = models.CharField(max_length=100)

    def __str__(self):
        return self.app_type

