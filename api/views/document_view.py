from rest_framework import viewsets
from api.models import Document
from api.serializers import DocumentSerializer

class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer