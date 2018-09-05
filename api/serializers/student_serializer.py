from rest_framework import serializers
from api.models import Student
from .user_serializer import UserSerializer

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = (
            'id',
            'url',
            'user'
        )