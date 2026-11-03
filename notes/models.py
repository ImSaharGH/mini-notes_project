from django.db import models

class Notes(models.Model):
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

