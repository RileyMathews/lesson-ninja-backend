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

    def get_queryset(self):
        if self.kwargs['get_single_user']:
            queryset = Student.objects.filter(user=request.user)
        else:
            queryset = Student.objects.all()

        return queryset
