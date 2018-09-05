from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.conf.urls import url
from api import views
router = DefaultRouter()

router.register('user', views.UserViewset)


urlpatterns = router.urls