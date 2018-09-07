from rest_framework import viewsets
from api.models import StudentLesson
from api.serializers import StudentLessonSerializer

class StudentLessonView(viewsets.ModelViewSet):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_teacher:
            print("teacher")
            queryset = StudentLesson.objects.filter(teacher=current_user.teacher)
        elif current_user.is_student:
            print("student")
            print(current_user.student)
            queryset = StudentLesson.objects.filter(student=current_user.student)
        else:
            queryset = StudentLesson.objects.all()

        return queryset