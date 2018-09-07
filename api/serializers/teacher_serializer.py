from rest_framework import serializers
from api.serializers import UserSerializer, StudentSerializer
from api.models import Teacher

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = (
            'id',
            'url',
            'bio',
            'street',
            'city',
            'region',
            'country',
            'zip_code',
            'user',
            'students'
        )
        depth = 1