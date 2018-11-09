from api.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset = [self.request.user]

        return queryset