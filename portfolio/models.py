from django.db import models

# Create your models here.

class Port (models.Model):
    title        = models.CharField (max_length = 100)
    description  = models.CharField (max_length = 255)
    summary      = models.CharField (max_length = 100)
