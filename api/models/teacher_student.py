from django.db import models
from .teacher import Teacher
from .student import Student

class TeacherStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    confirmed = models.BooleanField()

    def __str__(self):
        return f'{self.teacher.user.first_name} teaching {self.student.user.first_name}'