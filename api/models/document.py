from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    s3_url = models.CharField(max_length=500)