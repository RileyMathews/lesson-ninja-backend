from rest_framework import serializers
from api.models import StudentLesson

class StudentLessonReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentLesson
        fields = (
            'id',
            'url',
            'lesson',
            'student',
            'has_opened',
            'finished_on',
        )
        depth=2