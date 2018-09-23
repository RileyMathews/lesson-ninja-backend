from django.db import models
from .document import Document
from .lesson import Lesson

class LessonDocument(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("document", "lesson"),)