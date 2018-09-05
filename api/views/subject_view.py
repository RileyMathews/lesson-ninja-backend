from rest_framework import viewsets
from api.models import Subject
from api.serializers import SubjectSerializer

class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
