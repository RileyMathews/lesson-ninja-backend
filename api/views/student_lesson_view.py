from rest_framework import viewsets
from api.models import StudentLesson
from api.serializers import StudentLessonSerializer

class StudentLessonView(viewsets.ModelViewSet):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer