from rest_framework import serializers
from api.models import TeacherStudent

class TeacherStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherStudent
        fields = (
            'id',
            'url',
            'teacher',
            'student',
            'confirmed'
        )