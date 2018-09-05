from rest_framework import serializers
from api.models import StudentLesson

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