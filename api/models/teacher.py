from django.db import models
from .user import User
from .student import Student
from random import randint
import uuid

class Teacher(models.Model):
    connection_key = models.CharField(max_length=255, unique=True, default=uuid.uuid4())
    bio = models.CharField(max_length=500, blank=True)
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='TeacherStudent')

    def __str__(self):
        return f'teacher {self.user}'

    def generate_key(self):
        number = randint(1000, 9999)
        key = f'{self.user.username}#{number}'
        self.connection_key = key
