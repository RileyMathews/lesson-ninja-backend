from rest_framework import serializers
from api.models import Subject

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'url',
            'name',
            'description'
        )