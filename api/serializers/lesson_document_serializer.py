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
                queryset=LessonDocument.objects.all(),
                fields=('lesson', 'document')
            )
        ]