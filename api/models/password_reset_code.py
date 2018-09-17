from django.db import models
from .user import User
import uuid

class PasswordResetCode(models.Model):
    code = models.CharField(max_length=255, unique=True, default=uuid.uuid4())
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reset_code")

    def __str__(self):
        return str(self.code)