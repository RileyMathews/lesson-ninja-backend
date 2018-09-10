from rest_framework import serializers
from api.models import StudentLesson
from api.serializers import StudentSerializer, LessonSerializer


class StudentLessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentLesson
        fields = (
            'id',
            'url',
            'student',
            'lesson',
            'has_opened',
            'finished_on'
        )