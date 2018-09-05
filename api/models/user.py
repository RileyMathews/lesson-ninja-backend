from django.contrib.auth.models import AbstractUser
from django.db import models

"""
    module: user model
    author: riley mathews
    purpose: to create a custom model for the employer and crew member user that uses authentication
"""

class User(AbstractUser):
    is_teacher = models.BooleanField(blank=True, default=0)
    is_student = models.BooleanField(blank=True, default=0)

    def __str__(self):
        return f'{self.email} {self.first_name} {self.last_name}'