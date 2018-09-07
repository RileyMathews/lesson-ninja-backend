from rest_framework import viewsets
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        serializer = StudentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self, *args, **kwargs):
        if self.request.query_params.get('get_single_user', False):
            queryset = Student.objects.filter(user=self.request.user)
        elif self.request.query_params.get('username', ''):
            search_terms = self.request.query_params.get('username', '')
            queryset = Student.objects.all()
            queryset = [student for student in queryset if search_terms in student.user.username]
        else:
            queryset = Student.objects.all()

        return queryset
