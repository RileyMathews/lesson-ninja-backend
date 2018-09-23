from rest_framework import serializers
from api.models import StudentLesson
from api.serializers import StudentSerializer, LessonSerializer
from .student_lesson_read_serializer import StudentLessonReadSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.validators import UniqueTogetherValidator


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

        validators = [
            UniqueTogetherValidator(
                queryset=StudentLesson.objects.all(),
                fields=('student', 'lesson')
            )
        ]

    def to_representation(self, instance):
        serializer = StudentLessonReadSerializer(instance, context=self.context)
        return serializer.data