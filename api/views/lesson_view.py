from rest_framework import viewsets
from api.models import Lesson
from api.serializers import LessonSerializer
from rest_framework import status
from rest_framework.response import Response

class LessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def create(self, request):
        serializer = LessonSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(teacher=request.user.teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if self.request.query_params.get('filter_by_auth', False):
            queryset = Lesson.objects.filter(teacher = self.request.user.teacher)
        else:
            queryset = Lesson.objects.all()

        return queryset