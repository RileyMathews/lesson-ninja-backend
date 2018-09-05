from rest_framework import viewsets
from api.serializers import TeacherSerializer
from rest_framework import status
from rest_framework.response import Response
from api import models
from api import serializers


class TeacherView(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

    def create(self, request):
        serializer = TeacherSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)