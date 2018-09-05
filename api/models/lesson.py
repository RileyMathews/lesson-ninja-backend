from django.db import models
from .teacher import Teacher

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name