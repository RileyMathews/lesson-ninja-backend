from rest_framework import viewsets
from api.models import StudentLesson
from api.serializers import StudentLessonSerializer, StudentLessonReadSerializer

class StudentLessonView(viewsets.ModelViewSet):
    queryset = StudentLesson.objects.all()
    # serializer_class = StudentLessonSerializer

    def get_queryset(self):
        current_user = self.request.user
        queryset = StudentLesson.objects.all()
        if self.request.query_params.get("users", None):
            if current_user.is_teacher:
                teachers_lessons = current_user.teacher.lesson_set.all()
                queryset = StudentLesson.objects.all()
                queryset = [assignment for assignment in queryset if assignment.lesson in teachers_lessons]
            elif current_user.is_student:
                queryset = StudentLesson.objects.filter(student=current_user.student)
                
        return queryset

    def get_serializer_class(self):
        
        if self.request.method in ['GET']:
            
            return StudentLessonReadSerializer
            
        return StudentLessonSerializer