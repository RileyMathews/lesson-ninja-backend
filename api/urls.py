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
    path('connect/', views.connection_view),
    path('auth/change_password/', views.change_password),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

router.register('user', views.UserView)
router.register('student', views.StudentView)
router.register('teacher', views.TeacherView)
router.register('teacher_student', views.TeacherStudentView)
router.register('subject', views.SubjectView)
router.register('lesson', views.LessonView)
router.register('student_lesson', views.StudentLessonView)
router.register('document', views.DocumentView)
router.register('lesson_document', views.LessonDocumentView)


urlpatterns += router.urls