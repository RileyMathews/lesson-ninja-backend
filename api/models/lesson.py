from django.db import models
from .teacher import Teacher
from .document import Document

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document, through='LessonDocument')

    def __str__(self):
        return self.name