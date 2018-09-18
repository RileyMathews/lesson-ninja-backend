import json
from django.http import HttpResponse
from api.models import User

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.core.validators import validate_email, validate_unicode_slug
from django.core.exceptions import ValidationError

@csrf_exempt
def register_user(request):
    """Handles the creation of a new user for authentication
    Method args:
        request -- the full HTTP request object
    """
    errors_found = False

    req_body = json.loads(request.body.decode())

    all_users = User.objects.all()

    username_check = [user for user in all_users if user.username == req_body['username']]
    email_check = [user for user in all_users if user.email == req_body['email']]

    errors = dict()
    if username_check:
        errors["username"] = "This username is already in use"
        errors_found = True
    
    if email_check:
        errors["email"] = "This email is already in use"
        errors_found = True

    try:
        validate_email(req_body['email'])
    except ValidationError:
        errors_found = True
        errors["email"] = "Please enter a valid email address"

    try:
        validate_unicode_slug(req_body['username'])
    except ValidationError:
        errors_found = True
        errors["username"] = "please enter a valid username"
    

    if errors_found:
        response = json.dumps(errors)
    else:
        # make new user
        new_user = User.objects.create_user(
            username=req_body['username'],
            password=req_body['password'],
            email=req_body['email'],
            first_name=req_body['first_name'],
            last_name=req_body['last_name'],
            is_student=req_body['is_student'],
            is_teacher=req_body['is_teacher']
        )
        token = Token.objects.create(user=new_user)

        response = json.dumps({"token": token.key})

        send_mail(
            f"Welcome {req_body['first_name']}", 
            "Welcome to lesson Ninja! And thank you for trying this out. If you have any questions, concerns, or comments feel free to reach out to me at contact@lesson.ninja. Happy Learning!",
            "noreply@lesson.ninja",
            [new_user.email],
            fail_silently=False
        )


    return HttpResponse(response, content_type='application/json')
