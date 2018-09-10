from django.db import models
from .teacher import Teacher

class Document(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    s3_url = models.CharField(max_length=500)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name