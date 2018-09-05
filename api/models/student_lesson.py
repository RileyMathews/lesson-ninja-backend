from django.db import models
from .student import Student
from .lesson import Lesson

class StudentLesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    has_opened = models.BooleanField()
    finished_on = models.DateField(blank=True, null=True)
