from rest_framework import viewsets
from api.models import LessonDocument
from api.serializers import LessonDocumentSerializer

class LessonDocumentView(viewsets.ModelViewSet):
    queryset = LessonDocument.objects.all()
    serializer_class = LessonDocumentSerializer