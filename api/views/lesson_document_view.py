from rest_framework import viewsets
from api.models import LessonDocument
from api.serializers import LessonDocumentSerializer
from rest_framework.permissions import IsAuthenticated

class LessonDocumentView(viewsets.ModelViewSet):
    queryset = LessonDocument.objects.all()
    serializer_class = LessonDocumentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = LessonDocument.objects.all()
        # get url parameters
        lesson = self.request.query_params.get("lesson", None)
        document = self.request.query_params.get("document", None)
        # filter off those parameters
        if lesson and document:
            queryset = [item for item in queryset if item.lesson.id == int(lesson) and item.document.id == int(document)]
        # return queryset
        return queryset