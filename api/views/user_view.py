from api.models import User
from api.serializers import UserSerializer
from rest_framework import viewsets

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.query_params.get('get_single_user', False):
            queryset = [self.request.user]
        else:
            queryset = User.objects.all()

        return queryset