from rest_framework import serializers
from api.models import Document
from .teacher_serializer import TeacherSerializer

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    # teacher = TeacherSerializer(read_only=True)
    class Meta:
        model = Document
        fields = (
            'id',
            'url',
            's3_url',
            's3_key',
            'file_extension',
            'name',
            'notes',
            # 'teacher'
        )