from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.conf.urls import url
from api import views
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()

urlpatterns = [
    path('auth/register/', views.register_user),
    path('auth/login/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router.register('user', views.UserViewset)


urlpatterns += router.urls