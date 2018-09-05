from rest_framework import viewsets
from api.models import TeacherStudent
from api.serializers import TeacherStudentSerializer

class TeacherStudentView(viewsets.ModelViewSet):
    queryset = TeacherStudent.objects.all()
    serializer_class = TeacherStudentSerializer