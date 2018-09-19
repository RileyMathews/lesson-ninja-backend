
from rest_framework import serializers
from api.models import Lesson
from .teacher_serializer import TeacherSerializer
from .document_serializer import DocumentSerializer

class LessonSerializer(serializers.HyperlinkedModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = (
            'id',
            'url',
            'name',
            'description',
            'content',
            'teacher',
            'documents'
        )