from rest_framework import viewsets
from api.models import Document
from api.serializers import DocumentSerializer

class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self, request):
        serializer = DocumentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=request.user.teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)