from rest_framework import viewsets
from api.models import Document
from api.serializers import DocumentSerializer
from rest_framework import status
from rest_framework.response import Response

class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def create(self, request):
        serializer = DocumentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=request.user.teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        current_teacher = self.request.user.teacher
        queryset = Document.objects.filter(teacher=current_teacher)
        return queryset