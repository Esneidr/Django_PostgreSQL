from django.db import models

class Taks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

