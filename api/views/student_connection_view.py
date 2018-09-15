from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from api.models import Teacher, Student, TeacherStudent, User
import json

@permission_classes((IsAuthenticated, ))
@authentication_classes((TokenAuthentication, ))
@csrf_exempt
def connection_view(request):

    req_body = json.loads(request.body.decode())
    token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
    current_user = User.objects.get(auth_token=token)
    if current_user.is_student:
        teacher = Teacher.objects.get(connection_key=req_body["connection_key"])
        student = current_user.student

        connection_exists = teacher in student.teacher_set.all()
        print(connection_exists)
        if teacher in student.teacher_set.all():
            response = json.dumps({"error": "You're already connected"})
        else:
            new_connection = TeacherStudent.objects.create(
                teacher=teacher,
                student=student,
                confirmed=True
            )
            response = json.dumps({"sucsess": "It worked!"})
    else:
        response  = json.dumps({"error": "Only students may make a connection request. We really aren't sure how this happened..."})

    return HttpResponse(response, content_type="application/json")
