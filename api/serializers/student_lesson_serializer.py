from rest_framework import serializers
from api.models import StudentLesson
from api.serializers import StudentSerializer, LessonSerializer
from .student_lesson_read_serializer import StudentLessonReadSerializer


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

    def to_representation(self, instance):
        print(self)
        print(instance)
        serializer = StudentLessonReadSerializer(instance, context=self.context)
        return serializer.data