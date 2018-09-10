from rest_framework import serializers
from api.models import Document

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'url',
            's3_url',
            'name',
            'notes'
        )