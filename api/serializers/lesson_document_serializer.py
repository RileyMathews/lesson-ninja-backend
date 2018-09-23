from rest_framework import serializers
from api.models import LessonDocument
from rest_framework.validators import UniqueTogetherValidator

class LessonDocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = LessonDocument
        fields = (
            'id',
            'url',
            'lesson',
            'document',
        )

        validators = [
            UniqueTogetherValidator(
                queryset=StudentLesson.objects.all(),
                fields=('student', 'lesson')
            )
        ]