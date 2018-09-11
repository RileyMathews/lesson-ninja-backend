from rest_framework import viewsets
from api.models import TeacherStudent
from api.serializers import TeacherStudentSerializer

class TeacherStudentView(viewsets.ModelViewSet):
    queryset = TeacherStudent.objects.all()
    serializer_class = TeacherStudentSerializer

    def get_queryset(self):
        queryset = TeacherStudent.objects.all()
        # get url parameters
        teacher = self.request.query_params.get("teacher", None)
        student = self.request.query_params.get("student", None)
        # filter off those parameters
        if teacher and student:
            queryset = [item for item in queryset if item.teacher.id == int(teacher) and item.student.id == int(student)]
        # return queryset
        return queryset