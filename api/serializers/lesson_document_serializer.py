from rest_framework import serializers
from api.models import LessonDocument

class LessonDocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = LessonDocument
        fields = (
            'id',
            'url',
            'lesson',
            'document',
        )